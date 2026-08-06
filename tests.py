import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('book_name', ['Я', 'А' * 40])
    def test_add_new_book_valid_name_book_added(self, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)

        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize('book_name', ['', 'А' * 41])
    def test_add_new_book_invalid_name_book_not_added(self, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)

        assert collector.get_books_genre() == {}

    def test_add_new_book_same_book_twice_added_once(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        'book_name, genre',
        [
            ('Дюна', 'Фантастика'),
            ('Оно', 'Ужасы'),
            ('Шерлок Холмс', 'Детективы'),
        ]
    )
    def test_set_book_genre_valid_genre_genre_set(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)

        collector.set_book_genre(book_name, genre)

        assert collector.get_book_genre(book_name) == genre

    def test_get_book_genre_new_book_genre_is_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')

        assert collector.get_book_genre('Дюна') == ''

    def test_get_books_with_specific_genre_returns_only_books_of_selected_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Марсианин')
        collector.add_new_book('Оно')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Марсианин', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')

        books = collector.get_books_with_specific_genre('Фантастика')

        assert books == ['Дюна', 'Марсианин']

    def test_get_books_for_children_age_rating_books_not_returned(self):
        collector = BooksCollector()
        collector.add_new_book('Винни-Пух')
        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Винни-Пух', 'Мультфильмы')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        books = collector.get_books_for_children()

        assert books == ['Винни-Пух']

    def test_add_book_in_favorites_same_book_twice_added_once(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')

        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == ['Дюна']

    def test_delete_book_from_favorites_added_book_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')

        collector.delete_book_from_favorites('Дюна')

        assert 'Дюна' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_returns_added_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Марсианин')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Марсианин')

        assert collector.get_list_of_favorites_books() == ['Дюна', 'Марсианин']
