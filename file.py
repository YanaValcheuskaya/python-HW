def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Сохранить изменения',
          '8. Скопировать строку в файл',
          '9. Закончить работу', sep='\n')
    
    choice=int(input('введите номер меню: '))
    return choice

def work_with_phonebook():
    choise=show_menu()
    phone_book=read_txt('phonebook.txt')

    while choise!=9:
        if choise==1:
            pretty_print_phone_book(phone_book, True)
        elif choise==2:
            last_name=input('введите фамилию: ')
            pretty_print_phone_book (find_by_last_name(phone_book,last_name))
        elif choise==3:
            last_name=input('введите фамилию: ')
            new_number=input('введите новый номер: ')
            pretty_print_phone_book (change_number(phone_book,last_name,new_number))
        elif choise==4:
            last_name=input('введите фамилию: ')
            pretty_print_phone_book (delete_by_last_name(phone_book,last_name))
        elif choise==5:
            number=input('введите номер: ')
            pretty_print_phone_book (find_by_number(phone_book,number))
        elif choise==6:
            last_name=input('введите фамилию: ')
            first_name=input('введите имя: ')
            number=input('введите номер: ')
            desc=input('введите описание: ')
            pretty_print_phone_book(add_user(phone_book,str(last_name),str(first_name),str(number),str(desc)))
        elif choise==7:
            write_file('phonebook.txt',phone_book)
        elif choise==8:
            line_num=input('введите номер строки: ')
            filename=input('введите имя файла: ')
            copy_record(phone_book,int(line_num)-1,filename)

        choise = show_menu()

def find_by_last_name(phone_book,last_name):
    out=[]
    for i in phone_book:
        if i.get('Фамилия')==last_name:
            out.append(i)
    return out

def change_number(phone_book,last_name,new_number):
    out=[]
    for i in range(0,len(phone_book)):
        if phone_book[i].get('Фамилия')==last_name:
            phone_book[i]['Телефон']=new_number
            out.append(phone_book[i])
    # write_file('phonebook.txt',phone_book)
    return out
            

def delete_by_last_name(phone_book,last_name):
    out=[]
    index_del=[]
    for i in range(0,len(phone_book)):
        if phone_book[i].get('Фамилия')==last_name:
            out.append(phone_book[i])
            index_del.append(i)
    for i in index_del:
        del phone_book[i]

    return out

def find_by_number(phone_book,number):
    out=[]
    for i in phone_book:
        if i.get('Телефон')==str(number):
            out.append(i)
    return out

def find_by_line_num(phone_book,line_num):
    out=[]
    out.append(phone_book[line_num])
    return out

def add_user(phone_book,last_name='',first_name='',number='',desc=''):
    fields = ['Фамилия','Имя','Телефон','Описание',]
    record = [last_name,first_name,number,desc]
    phone_book.append(dict(zip(fields, record)))
    # write_file('phonebook.txt',phone_book)
    return phone_book

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия','Имя','Телефон','Описание',]
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.rstrip('\n').split(',')))
            phone_book.append(record)
    return phone_book

def copy_record(phone_book,line_num,filename):
    write_file(filename,find_by_line_num(phone_book,line_num),False)

def write_file(filename,phone_book,is_rewrite=True):
    if is_rewrite:
        open_mode = 'w'
    else:
        open_mode = 'a'
    with open(filename,open_mode,encoding='utf-8') as phout:
        for i in range (len(phone_book)):
            s=''
            if is_rewrite != True:
                s='\n'
            for v in phone_book[i].values():
                s+=v+','
            if i<len(phone_book)-1:
                phout.write(f'{s[:-1]}\n')
            else:
                phout.write(f'{s[:-1]}')

def pretty_print_phone_book(phone_book, is_print_index=False):
    if len(phone_book) == 0:
        print('данные отсутствуют')
    else:
        for i in range (len(phone_book)):
            s=''
            if is_print_index:
                s=str(i+1)+'\t'
            for v in phone_book[i].values():
                s+=v
                if len(v) < 8:
                    s+='\t\t'
                else:
                    s+='\t'
            print(s)

work_with_phonebook()
