def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.

    Parameter: lst: range
    """
    try:
        assert isinstance(lst, range), "parameter is not a list"
        assert all(isinstance(i, int) for i in lst), \
            "parameter is not a int of list"

        total_len = len(lst)
        bar_len = 100
        for i in lst:
            load = int((i + 1) / total_len * 100)
            prog = "█" * (int((i + 1) / total_len * bar_len))
            print(f"\r{load}%|{prog:<{bar_len}}| {i + 1}/{total_len}", end="")
            yield i

    except AssertionError as e:
        print(f"AssertionError: {e}")
