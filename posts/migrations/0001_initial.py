# Generated by Django 3.0.6 on 2020-06-30 16:12

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('cover', models.ImageField(upload_to=posts.models.sheet_upload_location, verbose_name='Answer Sheet')),
                ('template', models.FileField(blank=True, default='template.json', upload_to=posts.models.template_upload_location)),
                ('marker', models.ImageField(blank=True, default='omr_marker.jpg', upload_to=posts.models.template_upload_location)),
                ('q1', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True, verbose_name='Answer key:Q1')),
                ('q2', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q3', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q4', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q5', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q6', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q7', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q8', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q9', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q10', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q11', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q12', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q13', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q14', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q15', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q16', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q17', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q18', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q19', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q20', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q21', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q22', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q23', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q24', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q25', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q26', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q27', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q28', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q29', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q30', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q31', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q32', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q33', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q34', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q35', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q36', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q37', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q38', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q39', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q40', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'Exams Record 40 Questions',
            },
        ),
        migrations.CreateModel(
            name='Exams100',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('cover', models.ImageField(upload_to=posts.models.sheet_upload_location100, verbose_name='Answer Sheet')),
                ('template', models.FileField(blank=True, default='template.json', upload_to=posts.models.template_upload_location100)),
                ('marker', models.ImageField(blank=True, default='omr_marker.jpg', upload_to=posts.models.template_upload_location100)),
                ('q1', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True, verbose_name='Answer key:Q1')),
                ('q2', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q3', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q4', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q5', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q6', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q7', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q8', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q9', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q10', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q11', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q12', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q13', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q14', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q15', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q16', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q17', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q18', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q19', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q20', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q21', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q22', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q23', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q24', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q25', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q26', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q27', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q28', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q29', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q30', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q31', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q32', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q33', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q34', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q35', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q36', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q37', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q38', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q39', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q40', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q41', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q42', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q43', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q44', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q45', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q46', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q47', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q48', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q49', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q50', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q51', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q52', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q53', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q54', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q55', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q56', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q57', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q58', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q59', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q60', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q61', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q62', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q63', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q64', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q65', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q66', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q67', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q68', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q69', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q70', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q71', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q72', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q73', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q74', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q75', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q76', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q77', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q78', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q79', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q80', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q81', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q82', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q83', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q84', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q85', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q86', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q87', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q88', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q89', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q90', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q91', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q92', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q93', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q94', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q95', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q96', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q97', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q98', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q99', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
                ('q100', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'Exams Record 100 Questions',
            },
        ),
        migrations.CreateModel(
            name='ProcessedMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_title', models.CharField(max_length=20)),
                ('student_id', models.CharField(default='', max_length=15)),
                ('student_name', models.CharField(default='', max_length=50)),
                ('processed_image', models.ImageField(upload_to='')),
                ('final_marks', models.CharField(blank=True, max_length=20, null=True)),
                ('q1', models.CharField(max_length=4, null=True)),
                ('q2', models.CharField(max_length=4, null=True)),
                ('q3', models.CharField(max_length=4, null=True)),
                ('q4', models.CharField(max_length=4, null=True)),
                ('q5', models.CharField(max_length=4, null=True)),
                ('q6', models.CharField(max_length=4, null=True)),
                ('q7', models.CharField(max_length=4, null=True)),
                ('q8', models.CharField(max_length=4, null=True)),
                ('q9', models.CharField(max_length=4, null=True)),
                ('q10', models.CharField(max_length=4, null=True)),
                ('q11', models.CharField(max_length=4, null=True)),
                ('q12', models.CharField(max_length=4, null=True)),
                ('q13', models.CharField(max_length=4, null=True)),
                ('q14', models.CharField(max_length=4, null=True)),
                ('q15', models.CharField(max_length=4, null=True)),
                ('q16', models.CharField(max_length=4, null=True)),
                ('q17', models.CharField(max_length=4, null=True)),
                ('q18', models.CharField(max_length=4, null=True)),
                ('q19', models.CharField(max_length=4, null=True)),
                ('q20', models.CharField(max_length=4, null=True)),
                ('q21', models.CharField(max_length=4, null=True)),
                ('q22', models.CharField(max_length=4, null=True)),
                ('q23', models.CharField(max_length=4, null=True)),
                ('q24', models.CharField(max_length=4, null=True)),
                ('q25', models.CharField(max_length=4, null=True)),
                ('q26', models.CharField(max_length=4, null=True)),
                ('q27', models.CharField(max_length=4, null=True)),
                ('q28', models.CharField(max_length=4, null=True)),
                ('q29', models.CharField(max_length=4, null=True)),
                ('q30', models.CharField(max_length=4, null=True)),
                ('q31', models.CharField(max_length=4, null=True)),
                ('q32', models.CharField(max_length=4, null=True)),
                ('q33', models.CharField(max_length=4, null=True)),
                ('q34', models.CharField(max_length=4, null=True)),
                ('q35', models.CharField(max_length=4, null=True)),
                ('q36', models.CharField(max_length=4, null=True)),
                ('q37', models.CharField(max_length=4, null=True)),
                ('q38', models.CharField(max_length=4, null=True)),
                ('q39', models.CharField(max_length=4, null=True)),
                ('q40', models.CharField(max_length=4, null=True)),
            ],
            options={
                'verbose_name_plural': 'Processed Marks',
            },
        ),
        migrations.CreateModel(
            name='ProcessedMarks100',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_title', models.CharField(max_length=20)),
                ('student_id', models.CharField(default='', max_length=15)),
                ('student_name', models.CharField(default='', max_length=50)),
                ('processed_image', models.ImageField(upload_to='')),
                ('final_marks', models.CharField(blank=True, max_length=20, null=True)),
                ('q1', models.CharField(max_length=4, null=True)),
                ('q2', models.CharField(max_length=4, null=True)),
                ('q3', models.CharField(max_length=4, null=True)),
                ('q4', models.CharField(max_length=4, null=True)),
                ('q5', models.CharField(max_length=4, null=True)),
                ('q6', models.CharField(max_length=4, null=True)),
                ('q7', models.CharField(max_length=4, null=True)),
                ('q8', models.CharField(max_length=4, null=True)),
                ('q9', models.CharField(max_length=4, null=True)),
                ('q10', models.CharField(max_length=4, null=True)),
                ('q11', models.CharField(max_length=4, null=True)),
                ('q12', models.CharField(max_length=4, null=True)),
                ('q13', models.CharField(max_length=4, null=True)),
                ('q14', models.CharField(max_length=4, null=True)),
                ('q15', models.CharField(max_length=4, null=True)),
                ('q16', models.CharField(max_length=4, null=True)),
                ('q17', models.CharField(max_length=4, null=True)),
                ('q18', models.CharField(max_length=4, null=True)),
                ('q19', models.CharField(max_length=4, null=True)),
                ('q20', models.CharField(max_length=4, null=True)),
                ('q21', models.CharField(max_length=4, null=True)),
                ('q22', models.CharField(max_length=4, null=True)),
                ('q23', models.CharField(max_length=4, null=True)),
                ('q24', models.CharField(max_length=4, null=True)),
                ('q25', models.CharField(max_length=4, null=True)),
                ('q26', models.CharField(max_length=4, null=True)),
                ('q27', models.CharField(max_length=4, null=True)),
                ('q28', models.CharField(max_length=4, null=True)),
                ('q29', models.CharField(max_length=4, null=True)),
                ('q30', models.CharField(max_length=4, null=True)),
                ('q31', models.CharField(max_length=4, null=True)),
                ('q32', models.CharField(max_length=4, null=True)),
                ('q33', models.CharField(max_length=4, null=True)),
                ('q34', models.CharField(max_length=4, null=True)),
                ('q35', models.CharField(max_length=4, null=True)),
                ('q36', models.CharField(max_length=4, null=True)),
                ('q37', models.CharField(max_length=4, null=True)),
                ('q38', models.CharField(max_length=4, null=True)),
                ('q39', models.CharField(max_length=4, null=True)),
                ('q40', models.CharField(max_length=4, null=True)),
                ('q41', models.CharField(max_length=4, null=True)),
                ('q42', models.CharField(max_length=4, null=True)),
                ('q43', models.CharField(max_length=4, null=True)),
                ('q44', models.CharField(max_length=4, null=True)),
                ('q45', models.CharField(max_length=4, null=True)),
                ('q46', models.CharField(max_length=4, null=True)),
                ('q47', models.CharField(max_length=4, null=True)),
                ('q48', models.CharField(max_length=4, null=True)),
                ('q49', models.CharField(max_length=4, null=True)),
                ('q50', models.CharField(max_length=4, null=True)),
                ('q51', models.CharField(max_length=4, null=True)),
                ('q52', models.CharField(max_length=4, null=True)),
                ('q53', models.CharField(max_length=4, null=True)),
                ('q54', models.CharField(max_length=4, null=True)),
                ('q55', models.CharField(max_length=4, null=True)),
                ('q56', models.CharField(max_length=4, null=True)),
                ('q57', models.CharField(max_length=4, null=True)),
                ('q58', models.CharField(max_length=4, null=True)),
                ('q59', models.CharField(max_length=4, null=True)),
                ('q60', models.CharField(max_length=4, null=True)),
                ('q61', models.CharField(max_length=4, null=True)),
                ('q62', models.CharField(max_length=4, null=True)),
                ('q63', models.CharField(max_length=4, null=True)),
                ('q64', models.CharField(max_length=4, null=True)),
                ('q65', models.CharField(max_length=4, null=True)),
                ('q66', models.CharField(max_length=4, null=True)),
                ('q67', models.CharField(max_length=4, null=True)),
                ('q68', models.CharField(max_length=4, null=True)),
                ('q69', models.CharField(max_length=4, null=True)),
                ('q70', models.CharField(max_length=4, null=True)),
                ('q71', models.CharField(max_length=4, null=True)),
                ('q72', models.CharField(max_length=4, null=True)),
                ('q73', models.CharField(max_length=4, null=True)),
                ('q74', models.CharField(max_length=4, null=True)),
                ('q75', models.CharField(max_length=4, null=True)),
                ('q76', models.CharField(max_length=4, null=True)),
                ('q77', models.CharField(max_length=4, null=True)),
                ('q78', models.CharField(max_length=4, null=True)),
                ('q79', models.CharField(max_length=4, null=True)),
                ('q80', models.CharField(max_length=4, null=True)),
                ('q81', models.CharField(max_length=4, null=True)),
                ('q82', models.CharField(max_length=4, null=True)),
                ('q83', models.CharField(max_length=4, null=True)),
                ('q84', models.CharField(max_length=4, null=True)),
                ('q85', models.CharField(max_length=4, null=True)),
                ('q86', models.CharField(max_length=4, null=True)),
                ('q87', models.CharField(max_length=4, null=True)),
                ('q88', models.CharField(max_length=4, null=True)),
                ('q89', models.CharField(max_length=4, null=True)),
                ('q90', models.CharField(max_length=4, null=True)),
                ('q91', models.CharField(max_length=4, null=True)),
                ('q92', models.CharField(max_length=4, null=True)),
                ('q93', models.CharField(max_length=4, null=True)),
                ('q94', models.CharField(max_length=4, null=True)),
                ('q95', models.CharField(max_length=4, null=True)),
                ('q96', models.CharField(max_length=4, null=True)),
                ('q97', models.CharField(max_length=4, null=True)),
                ('q98', models.CharField(max_length=4, null=True)),
                ('q99', models.CharField(max_length=4, null=True)),
                ('q100', models.CharField(max_length=4, null=True)),
            ],
            options={
                'verbose_name_plural': 'Processed Marks 100',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(default='', max_length=15)),
                ('student_name', models.CharField(max_length=50)),
                ('student_email', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Students Record',
            },
        ),
    ]
