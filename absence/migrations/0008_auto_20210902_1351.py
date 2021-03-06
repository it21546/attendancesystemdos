# Generated by Django 3.1 on 2021-09-02 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absence', '0007_auto_20201208_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.CharField(choices=[('Πληροφορικής και Τηλεματικής', 'Πληροφορικής και Τηλεματικής'), ('Διαιτολογίας-Διατροφής', 'Διαιτολογίας-Διατροφής'), ('Γεωγραφίας', 'Γεωγραφίας'), ('Οικονομίας και Βιώσιμης Ανάπτυξης', 'Οικονομίας και Βιώσιμης Ανάπτυξης')], default='Πληροφορικής και Τηλεματικής', max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='post_und',
            field=models.CharField(choices=[('Προπτυχιακό', 'Προπτυχιακό'), ('Μεταπτυχιακό', 'Μεταπτυχιακό')], default='', max_length=100),
        ),
    ]
