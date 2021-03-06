# Generated by Django 3.2 on 2021-05-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_snippet_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='code',
            field=models.TextField(db_index=True, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='snippets', to='website.Tag', verbose_name='Тэг'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='title',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='Кол-во просмотров'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
