"""
迭代器模式 (Iterator Pattern) - 行为型模式

【解决的问题】
    1. 统一遍历接口：不同集合需要不同的遍历方式
    2. 隐藏内部实现：遍历时不暴露集合的内部结构
    3. 多种遍历方式：需要为同一个集合提供多种遍历方式

【应用场景】
    1. 需要遍历集合对象
    2. 需要统一多种集合的遍历方式
    3. 需要提供多种遍历策略

【优缺点】
    优点：
        - 简化集合遍历
        - 支持多种遍历方式
        - 隐藏集合内部实现
        - 符合单一职责原则
    缺点：
        - 增加类的数量
        - 对简单集合可能过度设计

【UML 结构】
    Iterator(迭代器接口) <-- ConcreteIterator(具体迭代器，持有 Aggregate)
    Aggregate(聚合接口) <-- ConcreteAggregate(具体聚合，创建迭代器)
"""

from abc import ABC, abstractmethod
from typing import List, Optional


# ===== 迭代器接口 =====
class Iterator(ABC):
    """迭代器接口"""
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass


# ===== 聚合接口 =====
class Aggregate(ABC):
    """聚合接口"""
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass


# ===== 具体迭代器 =====
class PlaylistIterator(Iterator):
    """播放列表迭代器（正序遍历）"""
    def __init__(self, songs: List[str]):
        self._songs = songs
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._songs)

    def next(self) -> Optional[str]:
        if self.has_next():
            song = self._songs[self._index]
            self._index += 1
            return song
        return None


class ShuffleIterator(Iterator):
    """随机播放迭代器"""
    def __init__(self, songs: List[str]):
        self._songs = songs.copy()
        import random
        random.shuffle(self._songs)
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._songs)

    def next(self) -> Optional[str]:
        if self.has_next():
            song = self._songs[self._index]
            self._index += 1
            return song
        return None


class ReverseIterator(Iterator):
    """倒序迭代器"""
    def __init__(self, songs: List[str]):
        self._songs = songs
        self._index = len(songs) - 1

    def has_next(self) -> bool:
        return self._index >= 0

    def next(self) -> Optional[str]:
        if self.has_next():
            song = self._songs[self._index]
            self._index -= 1
            return song
        return None


# ===== 具体聚合 =====
class Playlist(Aggregate):
    """播放列表"""
    def __init__(self):
        self._songs: List[str] = []

    def add_song(self, song: str):
        self._songs.append(song)

    def create_iterator(self) -> Iterator:
        """默认迭代器（正序）"""
        return PlaylistIterator(self._songs)

    def get_shuffle_iterator(self) -> Iterator:
        """随机播放迭代器"""
        return ShuffleIterator(self._songs)

    def get_reverse_iterator(self) -> Iterator:
        """倒序迭代器"""
        return ReverseIterator(self._songs)


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("迭代器模式演示：音乐播放器")
    print("=" * 50)

    # 创建播放列表
    playlist = Playlist()
    playlist.add_song("七里香 - 周杰伦")
    playlist.add_song("十年 - 陈奕迅")
    playlist.add_song("海阔天空 - Beyond")
    playlist.add_song("晴天 - 周杰伦")
    playlist.add_song("红豆 - 王菲")

    print("\n1. 顺序播放：")
    iterator = playlist.create_iterator()
    while iterator.has_next():
        print(f"  正在播放：{iterator.next()}")

    print("\n2. 倒序播放：")
    iterator = playlist.get_reverse_iterator()
    while iterator.has_next():
        print(f"  正在播放：{iterator.next()}")

    print("\n3. 随机播放：")
    iterator = playlist.get_shuffle_iterator()
    while iterator.has_next():
        print(f"  正在播放：{iterator.next()}")

    print("\n" + "=" * 50)
    print("实际工程应用：")
    print("  - Python for 循环底层（__iter__ / __next__）")
    print("  - 数据库游标遍历")
    print("  - 文件逐行读取")
    print("  - 多种遍历策略（正序、倒序、过滤等）")
    print("=" * 50)
