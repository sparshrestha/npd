from posts.usecases import GetExam40UseCase, GetExam100UseCase


class Exam40Mixin:
    def get_exam(self, *args, **kwargs):
        return GetExam40UseCase(
            exam_id=self.kwargs.get('exam_id')
        ).execute()


class Exam100Mixin:
    def get_exam(self, *args, **kwargs):
        return GetExam100UseCase(
            exam_id=self.kwargs.get('exam_id')
        ).execute()
