def upload_exam_cover_to(instance, filename):
    return '40/{}/input/sheets/{}'.format(
        instance.title,
        filename,
    )


def upload_exam_template_to(instance, filename):
    return '40/{}/input/{}'.format(
        instance.title,
        filename,
    )


def upload_exam_marker_to(instance, filename):
    return '40/{}/input/{}'.format(
        instance.title,
        filename,
    )


def upload_processed_marks_image_to(instance, filename):
    return '40/{}/output/{}'.format(
        instance.exam_title,
        filename,
    )


def upload_exam100_cover_to(instance, filename):
    return '100/{}/input/sheets/{}'.format(
        instance.title,
        filename,
    )


def upload_exam100_template_to(instance, filename):
    return '100/{}/input/{}'.format(
        instance.title,
        filename,
    )


def upload_exam100_marker_to(instance, filename):
    return '100/{}/input/{}'.format(
        instance.title,
        filename,
    )


def upload_100processed_marks_image_to(instance, filename):
    return '100/{}/output/{}'.format(
        instance.exam_title,
        filename,
    )
