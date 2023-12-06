# 第四章：迭代器与生成器

迭代是Python最强大的功能之一。初看起来，你可能会简单的认为迭代只不过是处理序列中元素的一种方法。 然而，绝非仅仅就是如此，还有很多你可能不知道的， 比如创建你自己的迭代器对象，在itertools模块中使用有用的迭代模式，构造生成器函数等等。 这一章目的就是向你展示跟迭代有关的各种常见问题。

Contents:

- [4.1 手动遍历迭代器](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p01_manually_consuming_iterator.html)
- [4.2 代理迭代](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p02_delegating_iteration.html)
- [4.3 使用生成器创建新的迭代模式](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p03_create_new_iteration_with_generators.html)
- [4.4 实现迭代器协议](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p04_implement_iterator_protocol.html)
- [4.5 反向迭代](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p05_iterating_in_reverse.html)
- [4.6 带有外部状态的生成器函数](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p06_define_generator_func_with_extra_state.html)
- [4.7 迭代器切片](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p07_taking_slice_of_iterator.html)
- [4.8 跳过可迭代对象的开始部分](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p08_skip_first_part_of_iterable.html)
- [4.9 排列组合的迭代](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p09_iterate_over_combination_or_permutation.html)
- [4.10 序列上索引值迭代](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p10_iterate_over_index_value_pairs_of_sequence.html)
- [4.11 同时迭代多个序列](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p11_iterate_over_multiple_sequences_simultaneously.html)
- [4.12 不同集合上元素的迭代](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p12_iterate_on_items_in_separate_containers.html)
- [4.13 创建数据处理管道](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p13_create_data_processing_pipelines.html)
- [4.14 展开嵌套的序列](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p14_flattening_nested_sequence.html)
- [4.15 顺序迭代合并后的排序迭代对象](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p15_iterate_in_sorted_order_over_merged_sorted_iterables.html)
- [4.16 迭代器代替while无限循环](https://python3-cookbook.readthedocs.io/zh-cn/latest/c04/p16_replace_infinite_while_loops_with_iterator.html)