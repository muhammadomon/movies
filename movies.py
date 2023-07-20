def movies():
    arr=[{
        'name' : 'Qasoskorlar 4',
        'year' : '2020',
        'id' : '192.168.1.1'
    },
    {
        'name' : 'Jinoyat alomatlari',
        'year' : '2023',
        'id' : '192.168.1.2'
    },
    {
        'name' : 'Joker',
        'year' : '2019',
        'id' : '192.168.1.3'
    },
    {
        'name' : 'Jon Uik 3',
        'year' : '2019',
        'id' : '192.168.1.4'
    },
    {
        'name' : "Assasin topshirig'i",
        'year' : '2023',
        'id' : '192.168.1.5'
    }]

    return arr


def search_movie():
    arr=movies()
    name_or_id=input("1.Nomi orqali izlash \n2.ID orqali izlash: ")
    if name_or_id==1:
        name=input('Film nomi: ')
        for i in arr:
            if i['name']==name:
                return i
            
    if name_or_id==2:
        id=input('Film id kiriting: ')
        for i in arr:
            if i['id']==id:
                return i
            


