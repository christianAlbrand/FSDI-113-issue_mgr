from django.db import migrations
def reverse_populate_status(apps, schema_editor):
    Status = apps.get_model("issues", "Status")
    Status.objects.all().delete()

def reverse_populate_priority(apps, schema_editor):
    Populate_priority = apps.get_model("issues", "Priority_level")
    Populate_priority.objects.all().delete()

def populate_status(apps, schemaeditor):
    entries = [
        "To Do",
        "In Progress",
        "Done"
    ]
    Status = apps.get_model("issues", "Status")
    for value in entries:
        status_obj = Status(name=value)
        status_obj.save()

def populate_priority(apps, schemaeditor):
    entries = [
        "Low",
        "Medium",
        "High"
    ]
    Populate_priority = apps.get_model("issues", "Priority_level")
    for value in entries:
        priority_obj = Populate_priority(name=value)
        priority_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_remove_priority_level_description_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_status, reverse_code=reverse_populate_status),
        migrations.RunPython(populate_priority, reverse_code=reverse_populate_priority)
    ]
