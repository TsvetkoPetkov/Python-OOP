from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self) -> None:
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document:Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        searched_category = next(filter(lambda x: x.id == category_id, self.categories))

        searched_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        searched_topic = next(filter(lambda x: x.id == topic_id, self.topics))

        searched_topic.topic = new_topic
        searched_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        searched_document = next(filter(lambda x: x.id == document_id, self.documents))

        searched_document.file_name = new_file_name

    def delete_category(self, category_id: int) -> None:
        category_to_delete = next(filter(lambda x: x.id == category_id, self.categories))

        self.categories.remove(category_to_delete)

    def delete_topic(self, topic_id: int) -> None:
        topic_to_delete = next(filter(lambda x: x.id == topic_id, self.topics))

        self.topics.remove(topic_to_delete)

    def delete_document(self, document_id: int) -> None:
        document_to_delete = next(filter(lambda x: x.id == document_id, self.documents))

        self.documents.remove(document_to_delete)

    def get_document(self, document_id: int) -> Document:
        document_to_get = next(filter(lambda x: x.id == document_id, self.documents))

        return document_to_get

    def __repr__(self):
        result = ''

        for d in self.documents:
            result += f"{d}\n"

        return result
