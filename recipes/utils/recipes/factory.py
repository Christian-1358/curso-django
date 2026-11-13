from random import choice

from faker import Faker


fake = Faker('pt_BR')

RECIPE_IMAGES = (
    'https://images.unsplash.com/photo-1546069901-ba9599a7e63c',
    'https://images.unsplash.com/photo-1504674900247-0877df9cc836',
    'https://images.unsplash.com/photo-1490645935967-10de6ba17061',
    'https://images.unsplash.com/photo-1547592180-85f173990554',
    'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38',
)


def make_recipe():
    return {
        'title':fake.random_number(digits=2, fix_len=True),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': f'{choice(RECIPE_IMAGES)}?auto=format&fit=crop&w=900&h=506&q=80',
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())