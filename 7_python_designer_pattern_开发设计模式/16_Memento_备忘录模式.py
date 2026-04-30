"""
备忘录模式 (Memento Pattern) - 行为型模式

【解决的问题】
    1. 状态保存和恢复：需要保存对象状态并在后续恢复
    2. 不破坏封装：保存状态时不暴露对象内部结构
    3. 撤销操作：支持多级撤销

【应用场景】
    1. 游戏存档/读档
    2. 编辑器撤销/重做
    3. 事务回滚
    4. 快照恢复

【优缺点】
    优点：
        - 不破坏封装即可保存状态
        - 简化发起者职责
        - 支持多级撤销
    缺点：
        - 可能消耗大量内存
        - 需要管理备忘录的生命周期

【UML 结构】
    Originator(发起者，创建 Memento) --> Memento(备忘录，存储状态)
    Caretaker(管理者，管理 Memento 列表) --> Memento
"""

from typing import List


# ===== 备忘录 =====
class Memento:
    """备忘录 - 存储游戏状态"""
    def __init__(self, level: int, hp: int, position: str):
        self._level = level
        self._hp = hp
        self._position = position

    def get_state(self):
        return self._level, self._hp, self._position


# ===== 发起者 =====
class GameCharacter:
    """游戏角色 - 发起者"""
    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.hp = 100
        self.position = "新手村"

    def fight(self, damage: int):
        """战斗 - 改变状态"""
        self.hp -= damage
        if self.hp <= 0:
            print(f"  {self.name} 阵亡！")
        else:
            print(f"  {self.name} 受到 {damage} 点伤害，剩余 HP: {self.hp}")

    def level_up(self):
        """升级"""
        self.level += 1
        self.hp = 100
        print(f"  {self.name} 升级！等级: {self.level}, HP 回满")

    def move_to(self, position: str):
        """移动"""
        self.position = position
        print(f"  {self.name} 移动到 {position}")

    def save(self) -> Memento:
        """保存当前状态到备忘录"""
        print(f"  [保存] 等级:{self.level} HP:{self.hp} 位置:{self.position}")
        return Memento(self.level, self.hp, self.position)

    def restore(self, memento: Memento):
        """从备忘录恢复状态"""
        self.level, self.hp, self.position = memento.get_state()
        print(f"  [恢复] 等级:{self.level} HP:{self.hp} 位置:{self.position}")

    def __str__(self):
        return f"{self.name} | 等级:{self.level} HP:{self.hp} 位置:{self.position}"


# ===== 管理者 =====
class SaveManager:
    """存档管理器 - 管理者"""
    def __init__(self):
        self._saves: List[Memento] = []

    def add_save(self, memento: Memento):
        self._saves.append(memento)

    def get_save(self, index: int) -> Memento:
        return self._saves[index]

    def get_latest_save(self) -> Memento:
        return self._saves[-1] if self._saves else None


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("备忘录模式演示：游戏存档系统")
    print("=" * 50)

    # 创建角色
    hero = GameCharacter("勇者")
    save_manager = SaveManager()

    print(f"\n初始状态：{hero}")

    # 游戏进程
    print("\n1. 冒险开始...")
    hero.move_to("黑暗森林")
    hero.fight(30)

    # 存档点 1
    print("\n2. 遇到 BOSS 前存档：")
    save_manager.add_save(hero.save())

    print("\n3. 挑战 BOSS...")
    hero.fight(80)  # 受到重创
    print(f"当前状态：{hero}")

    print("\n4. 读档回到 BOSS 前：")
    hero.restore(save_manager.get_latest_save())

    print("\n5. 这次先练级：")
    hero.level_up()
    hero.move_to("黑暗森林")
    hero.fight(80)
    print(f"最终状态：{hero}")

    print("\n" + "=" * 50)
    print("实际工程应用：")
    print("  - 文本编辑器撤销/重做")
    print("  - 游戏存档系统")
    print("  - 数据库事务回滚")
    print("  - Git 版本控制")
    print("=" * 50)
