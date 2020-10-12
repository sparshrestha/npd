import os

from OMRchecker import OMRChecker


class ProcessAllExamsUseCase:
    """
    Use this to process all exams at once
    """

    def __init__(self, folder: str):
        self._directory_path = folder

    def execute(self):
        self._factory()

    def _factory(self):
        # 1. get list of sub folder
        exams_folders = os.listdir(self._directory_path)

        # 2. process all exam_folders
        for exam in exams_folders:
            base_dir = '{}/{}'.format(
                self._directory_path,
                exam
            )

            input_dir = '{}/input'.format(
               base_dir
            )
            output_dir = '{}/output_dir'.format(
                base_dir
            )
            OMRChecker(
                input_dir=[input_dir],
                output_dir=output_dir
            ).execute()
