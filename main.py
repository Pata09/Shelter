import pandas as pd
import streamlit as st




class AnimalShelter:

    def __init__(self, name):
        self.name = name
        self.cats = {}
        self.dogs = {}

    def add_cat(self, Cat):
        with open('cats.csv', 'a') as out:
            out.write(Cat.__repr__() + "\n")


    def add_dog(self, Dog):

        with open('dogs.csv', 'a') as out:
            out.write(Dog.__repr__()+ "\n")


    def show_cats(self):

        df = pd.read_csv('cats.csv',index_col='Numer chipu')

        return df

    def show_dogs(self):

        df = pd.read_csv('dogs.csv',index_col='Numer chipu')

        return df

    def cats_to_csv(self):
        with open('cats.csv', 'a') as f:
            for key in self.cats.keys():
                f.write("%s,%s\n" % (key, self.cats[key]))

    def dogs_to_csv(self):
        with open('dogs.csv', 'a') as f:
            for key in self.dogs.keys():
                f.write("%s,%s\n" % (key, self.dogs[key]))

    def __repr__(self):
        return f'Animal Shelter {self.name}. We have {len(self.cats)} cats, and {len(self.dogs)} dogs.'



class Animal:

    def __init__(self, chip_code, name, age, colour, health):
        self.chip_code = chip_code
        self.name = name
        self.age = age
        self.colour = colour
        self.health = health


class Cat(Animal):

    def __init__(self, chip_code,  name, age, colour, health, race):
        super().__init__(chip_code, name, age, colour, health)
        self.race = race

    def __repr__(self):
        return f'{self.chip_code},{self.name},{self.colour},{self.age},{self.health},{"nie" if self.race == False else "tak" }'


class Dog(Animal):

    def __init__(self, chip_code,  name, age, colour, health, race, trained):
        super().__init__(chip_code, name, age, colour, health)
        self.race = race
        self.trained = trained

    def __repr__(self):
        return f'{self.chip_code},{self.name},{self.colour},{self.age},{self.health},{"nie" if self.race == False else "tak" },{"nie" if self.trained == False else "tak"}'


shelter1 = AnimalShelter("Schorniko w Michałowicach")
st.title('Rejestr zwierząt - Schronisko Michałowice')
st.sidebar.title('Menu')
chosen_animal = st.sidebar.radio('Wybierz rejestr:',('Koty','Psy'))

if chosen_animal == 'Koty':
    show_c = st.sidebar.button('Pokaż rejestr')
    if show_c:
        st.dataframe(shelter1.show_cats())
    st.subheader('Dodaj zwierzę do rejestru')
    with st.form('cat_form'):
        cat_id = st.number_input('Numer chipu:',step=1)
        cat_name = st.text_input('Imię:')
        cat_age = st.number_input('Wiek:',step=1)
        cat_color = st.text_input('Kolor:')
        cat_health = st.text_input('Dolegliwości:')
        st.caption('*Pole nie jest wymagane')
        cat_race = st.checkbox('Rasowy')
        submit_button = st.form_submit_button('Potwierdź')
        if submit_button:
            cat1 = Cat(cat_id,cat_name,cat_age,cat_color,cat_health,cat_race)
            shelter1.add_cat(cat1)
            st.caption('Zwierzę zostało dodane do rejestru.')

else:
    show_d = st.sidebar.button('Pokaż rejestr')
    st.subheader('Dodaj zwierzę do rejestru')
    if show_d:
        st.dataframe(shelter1.show_dogs())
    with st.form('dog_form'):
        dog_id = st.number_input('Numer chipu:',step=1)
        dog_name = st.text_input('Imię:')
        dog_age = st.number_input('Wiek:',step=1)
        dog_color = st.text_input('Kolor:')
        dog_health = st.text_input('Dolegliwości:')
        st.caption('*Pole nie jest wymagane')
        dog_race = st.checkbox('Rasowy')
        dog_training = st.checkbox('Wytresowany')
        submit_button = st.form_submit_button('Potwierdź')
        if submit_button:
            dog1 = Dog(dog_id,dog_name,dog_age,dog_color,dog_health,dog_race,dog_training)
            shelter1.add_dog(dog1)
            st.caption('Zwierzę zostało dodane do rejestru.')
