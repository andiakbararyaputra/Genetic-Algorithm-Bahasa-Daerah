import random
from dataclasses import dataclass, field


ACEH_DICTIONARY = [
    {"aceh": "peugah", "indonesia": "berkata"},
    {"aceh": "jak", "indonesia": "pergi"},
    {"aceh": "pue", "indonesia": "apa"},
    {"aceh": "soe", "indonesia": "siapa"},
    {"aceh": "rumoh", "indonesia": "rumah"},
    {"aceh": "bu", "indonesia": "nasi"},
    {"aceh": "ie", "indonesia": "air"},
    {"aceh": "sira", "indonesia": "garam"},
    {"aceh": "manok", "indonesia": "ayam"},
    {"aceh": "kupi", "indonesia": "kopi"},
    {"aceh": "droeneuh", "indonesia": "kamu"},
    {"aceh": "lon", "indonesia": "saya"},
]

GENE_POOL = "abcdefghijklmnopqrstuvwxyz"


@dataclass
class GAState:
    target: str | None = None
    population: list[str] = field(default_factory=list)
    fitness_scores: list[int] = field(default_factory=list)
    roulette_result: list[str] = field(default_factory=list)
    crossover_pairs: list[tuple[str, str, str, str]] = field(default_factory=list)
    mutation_result: list[str] = field(default_factory=list)
    new_population: list[str] = field(default_factory=list)


class GeneticAlgorithmAceh:
    def __init__(self, population_size: int = 8, mutation_rate: float = 0.2) -> None:
        self.population_size = population_size
        self.mutation_rate = mutation_rate

    @staticmethod
    def random_word(length: int) -> str:
        return "".join(random.choice(GENE_POOL) for _ in range(length))

    def initialize_population(self, target: str) -> list[str]:
        return [self.random_word(len(target)) for _ in range(self.population_size)]

    @staticmethod
    def calculate_fitness(individual: str, target: str) -> int:
        return sum(1 for i, c in enumerate(individual) if c == target[i])

    def calculate_all_fitness(self, population: list[str], target: str) -> list[int]:
        return [self.calculate_fitness(ind, target) for ind in population]

    def roulette_selection(self, population: list[str], fitness_scores: list[int]) -> list[str]:
        # +1 supaya individu dengan fitness 0 tetap punya peluang terpilih.
        adjusted_scores = [score + 1 for score in fitness_scores]
        total = sum(adjusted_scores)
        selected = []
        for _ in range(len(population)):
            pick = random.uniform(0, total)
            current = 0.0
            for individual, score in zip(population, adjusted_scores):
                current += score
                if current >= pick:
                    selected.append(individual)
                    break
        return selected

    @staticmethod
    def crossover(parent1: str, parent2: str) -> tuple[str, str]:
        if len(parent1) == 1:
            return parent1, parent2
        point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2

    def mutate(self, individual: str) -> str:
        chars = list(individual)
        for i in range(len(chars)):
            if random.random() < self.mutation_rate:
                chars[i] = random.choice(GENE_POOL)
        return "".join(chars)

    def generate_new_population(self, selected: list[str]) -> tuple[list[str], list[tuple[str, str, str, str]], list[str]]:
        crossover_pairs = []
        children = []
        for i in range(0, len(selected), 2):
            parent1 = selected[i]
            parent2 = selected[(i + 1) % len(selected)]
            child1, child2 = self.crossover(parent1, parent2)
            crossover_pairs.append((parent1, parent2, child1, child2))
            children.extend([child1, child2])

        children = children[: len(selected)]
        mutated = [self.mutate(child) for child in children]
        return mutated, crossover_pairs, children

    def run_one_generation(self, target: str) -> GAState:
        state = GAState(target=target)
        state.population = self.initialize_population(target)
        state.fitness_scores = self.calculate_all_fitness(state.population, target)
        state.roulette_result = self.roulette_selection(state.population, state.fitness_scores)
        state.new_population, state.crossover_pairs, pre_mutation = self.generate_new_population(state.roulette_result)
        state.mutation_result = [f"{before} -> {after}" for before, after in zip(pre_mutation, state.new_population)]
        return state


def tampilkan_kamus() -> None:
    print("\n=== Kamus Bahasa Aceh ===")
    for idx, entry in enumerate(ACEH_DICTIONARY, start=1):
        print(f"{idx}. {entry['aceh']} = {entry['indonesia']}")


def cari_kata() -> str | None:
    kata = input("Peulheueh kata (Aceh/Indonesia): ").strip().lower()
    hasil = [
        entry
        for entry in ACEH_DICTIONARY
        if entry["aceh"].lower() == kata or entry["indonesia"].lower() == kata
    ]

    if not hasil:
        print("Kata hana na lam kamus.")
        return None

    entry = hasil[0]
    print(f"Hasil: {entry['aceh']} = {entry['indonesia']}")
    print(f"Target GA ka dipeugot ke kata Aceh: {entry['aceh']}")
    return entry["aceh"]


def print_population(population: list[str], title: str) -> None:
    print(f"\n=== {title} ===")
    if not population:
        print("Data goh na. Jalankan GA sigoe lom.")
        return
    for i, individual in enumerate(population, start=1):
        print(f"{i}. {individual}")


def print_fitness(population: list[str], fitness_scores: list[int], target: str | None) -> None:
    print("\n=== Nilai Fitness ===")
    if not population or not fitness_scores or not target:
        print("Data fitness han jeuet ditampe. Jalankan proses sesuai urutan.")
        return
    for i, (individual, score) in enumerate(zip(population, fitness_scores), start=1):
        print(f"{i}. {individual} -> fitness {score}/{len(target)}")


def print_roulette(selected: list[str]) -> None:
    print_population(selected, "Hasil Seleksi Roulette")


def print_crossover(crossover_pairs: list[tuple[str, str, str, str]]) -> None:
    print("\n=== Cross Over (Silang) ===")
    if not crossover_pairs:
        print("Data crossover hana na. Jalankan proses sesuai urutan.")
        return
    for i, (p1, p2, c1, c2) in enumerate(crossover_pairs, start=1):
        print(f"Pasangan {i}: {p1} x {p2}")
        print(f"  -> Anak1: {c1}")
        print(f"  -> Anak2: {c2}")


def print_mutation(mutation_result: list[str]) -> None:
    print("\n=== Mutasi ===")
    if not mutation_result:
        print("Data mutasi hana na. Jalankan proses sesuai urutan.")
        return
    for i, item in enumerate(mutation_result, start=1):
        print(f"{i}. {item}")


def pilih_target() -> str:
    print("\nPilih target kata Aceh nibak kamus:")
    for idx, entry in enumerate(ACEH_DICTIONARY, start=1):
        print(f"{idx}. {entry['aceh']} ({entry['indonesia']})")
    while True:
        pilihan = input("Nomor target: ").strip()
        if pilihan.isdigit() and 1 <= int(pilihan) <= len(ACEH_DICTIONARY):
            return ACEH_DICTIONARY[int(pilihan) - 1]["aceh"]
        print("Pilihan hana sah, coba lom.")


def tampilkan_menu() -> None:
    print("\n========== MENU UTAMA ==========")
    print("1. Tampilkan Kamus")
    print("2. Cari Kata")
    print("3. Jalankan Algoritma Genetika")
    print("4. Tampilkan Populasi")
    print("5. Nilai Fitness")
    print("6. Seleksi Roulette")
    print("7. Cross Over")
    print("8. Mutasi")
    print("9. Generasi Baru")
    print("10. Keluar")


def main() -> None:
    ga = GeneticAlgorithmAceh()
    state = GAState()

    print("Aplikasi GA Kamus Bahasa Aceh")
    print("Keu tugas Rekayasa Komputasional")

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_kamus()
        elif pilihan == "2":
            target = cari_kata()
            if target:
                state.target = target
        elif pilihan == "3":
            target = state.target or pilih_target()
            state = ga.run_one_generation(target)
            print(f"\nGA ka dijalankan untuk target: {target}")
            print("Satu generasi lengkap ka diproses (fitness, roulette, crossover, mutasi, evaluasi).")
            print_population(state.population, "Populasi Awal")
            print_fitness(state.population, state.fitness_scores, state.target)
            print_roulette(state.roulette_result)
            print_crossover(state.crossover_pairs)
            print_mutation(state.mutation_result)
            print_population(state.new_population, "Populasi Generasi Baru")
        elif pilihan == "4":
            print_population(state.population, "Populasi Awal")
            print_population(state.new_population, "Populasi Generasi Baru")
        elif pilihan == "5":
            print_fitness(state.population, state.fitness_scores, state.target)
        elif pilihan == "6":
            print_roulette(state.roulette_result)
        elif pilihan == "7":
            print_crossover(state.crossover_pairs)
        elif pilihan == "8":
            print_mutation(state.mutation_result)
        elif pilihan == "9":
            print_population(state.new_population, "Generasi Baru")
            if state.new_population and state.target:
                new_fitness = ga.calculate_all_fitness(state.new_population, state.target)
                print("\nEvaluasi Fitness Generasi Baru:")
                for i, (individual, score) in enumerate(zip(state.new_population, new_fitness), start=1):
                    print(f"{i}. {individual} -> fitness {score}/{len(state.target)}")
        elif pilihan == "10":
            print("Teurimong geunaseh. Program selesai.")
            break
        else:
            print("Pilihan hana sah. Coba lom.")


if __name__ == "__main__":
    main()
