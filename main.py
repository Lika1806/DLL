import linked_list

def test():
    my_list = linked_list.LinkedList()
    my_list.display()
    print(my_list.is_empty())
    my_list.append('Data 0')
    my_list.append('appended Data')   
    my_list.prepend('prepended Data')
    my_list.insert_after('Data 0', 'Data inserted after "Data 0"')
    my_list.insert_before('Data 0', 'Data insterted before "Data 0"')
    my_list.append('1')
    my_list.append('2')
    my_list.append('3')
    my_list.delete('3')
    my_list.display()
#    my_list.delete('AAA')


test()



