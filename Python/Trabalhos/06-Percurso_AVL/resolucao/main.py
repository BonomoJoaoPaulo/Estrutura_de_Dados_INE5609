from AVL import AVL 

example_three = AVL()
number_of_elements = int(input())

for e in range(number_of_elements):
    new_element = int(input())
    example_three.insere(new_element)

example_three.imprime_pre_ordem(example_three)
print("")
example_three.imprime_em_ordem(example_three)
print("")
example_three.imprime_pos_ordem(example_three)
