class NPC:
    def __init__(self, name: str, level: int, health: int, fraction: str, hostile: bool):
        # ініц пол кл
        self.name = name
        self.level = level
        self.health = health
        self.fraction = fraction
        self.hostile = hostile

    def __eq__(self, other):
        # пер ідент об
        if isinstance(other, NPC):
            return (self.name == other.name and
                    self.level == other.level and
                    self.health == other.health and
                    self.fraction == other.fraction and
                    self.hostile == other.hostile)
        return False

    def __repr__(self):
        # форм вив ряд
        return f"NPC({self.name}, рівень:{self.level}, хп:{self.health}, фракція:{self.fraction}, ворог:{self.hostile})"


if __name__ == "__main__":
    # ств мас об
    npcs = [
        NPC("Гаррі", 10, 100, "Торговці", False),
        NPC("Орк", 15, 200, "Монстри", True),
        NPC("Гоблін", 10, 150, "Монстри", True),  # Однаковий рівень з Гаррі, але більше ХП
        NPC("Ельф", 20, 180, "Вартові", False),
        NPC("Троль", 15, 300, "Монстри", True)  # Однаковий рівень з Орком, але більше ХП
    ]

    print("--- Початковий масив ---")
    for npc in npcs:
        print(npc)

    # сорт мас об (рівень: зростання, хп: спадання)
    npcs.sort(key=lambda x: (x.level, -x.health))

    print("\n--- Відсортований масив ---")
    for npc in npcs:
        print(npc)

    # шук зад об
    target_npc = NPC("Гоблін", 10, 150, "Монстри", True)

    print(f"\nШукаємо: {target_npc}")
    if target_npc in npcs:
        # вив рез пош
        print("Результат: Об'єкт успішно знайдено в масиві!")
    else:
        print("Результат: Об'єкт не знайдено.")