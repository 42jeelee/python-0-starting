ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = "World!"

tmp = list(ft_tuple)
tmp[1] = "Korea!"
ft_tuple = tuple(tmp)

ft_set.remove("tutu!")
ft_set.add("Seoul!")

ft_dict["Hello"] = "42Seoul!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
