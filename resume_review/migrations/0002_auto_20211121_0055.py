# Generated by Django 3.2.8 on 2021-11-21 05:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resume_review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(max_length=255)),
                ('comment', models.TextField(null=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='department',
        ),
        migrations.RemoveField(
            model_name='reviewer',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='reviewer',
            name='rate',
        ),
        migrations.AddField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default='user.png', null=True, upload_to='profile_pic'),
        ),
        migrations.AddField(
            model_name='order',
            name='finished_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='reviewer',
            name='delivery_time',
            field=models.CharField(choices=[('delivery_1', 'One week'), ('delivery_2', 'Two weeks'), ('delivery_3', 'Three weeks'), ('delivery_4', 'Four weeks or more')], default='delivery_1', max_length=255),
        ),
        migrations.AlterField(
            model_name='account',
            name='academic',
            field=models.CharField(choices=[('Freshmen', 'Freshmen'), ('Sophomore', 'Sophomore'), ('Junior', 'Junior'), ('Senior', 'Senior'), ('Graduate', 'Graduate')], max_length=255),
        ),
        migrations.AlterField(
            model_name='account',
            name='major',
            field=models.CharField(choices=[('Accounting', 'Accounting'), ('Auditing & Financial Reporting', 'Auditing & Financial Reporting'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Amer Stud & Museum Stud', 'Amer Stud & Museum Stud'), ('American Studies', 'American Studies'), ('Anatomy', 'Anatomy'), ('Anesthesiology', 'Anesthesiology'), ('Applied Anatomy', 'Applied Anatomy'), ('Anthropology', 'Anthropology'), ('Applied Mathematics', 'Applied Mathematics'), ('Applied Physics', 'Applied Physics'), ('Architecture', 'Architecture'), ('Art Education', 'Art Education'), ('Art History', 'Art History'), ('Arts In Technical Age', 'Arts In Technical Age'), ('Art History & Museum Studies', 'Art History & Museum Studies'), ('Art Studio', 'Art Studio'), ('Asian Civilization', 'Asian Civilization'), ('Asian Studies', 'Asian Studies'), ('Astronomy', 'Astronomy'), ('Comp/Info Sci (Ms-Columbus)', 'Comp/Info Sci (Ms-Columbus)'), ('Banking And Finance', 'Banking And Finance'), ('Applied Social Science', 'Applied Social Science'), ('Biochemistry', 'Biochemistry'), ('Biomedical Entrepreneurship', 'Biomedical Entrepreneurship'), ('Bioethics', 'Bioethics'), ('Bioscience Entrepreneurship', 'Bioscience Entrepreneurship'), ('Biometry', 'Biometry'), ('Biology', 'Biology'), ('Biomedical Sciences', 'Biomedical Sciences'), ('Biochemical Research', 'Biochemical Research'), ('Adult Clinical Psychology', 'Adult Clinical Psychology'), ('Cell Biology', 'Cell Biology'), ('Critical Care Nursing', 'Critical Care Nursing'), ('Child Clinical Psychology', 'Child Clinical Psychology'), ('Chemistry', 'Chemistry'), ('Chinese', 'Chinese'), ('Community Health Nursing', 'Community Health Nursing'), ('Childhood Studies', 'Childhood Studies'), ('Computing And Info Science', 'Computing And Info Science'), ('Classics', 'Classics'), ('Comparative Literature', 'Comparative Literature'), ('Computer Science', 'Computer Science'), ('Ceramic And Materials Science', 'Ceramic And Materials Science'), ('Certificate In Non Profit Mgmt', 'Certificate In Non Profit Mgmt'), ('Cognitive Science', 'Cognitive Science'), ('Communication Sciences', 'Communication Sciences'), ('Cell Physiology', 'Cell Physiology'), ('Clinical Research', 'Clinical Research'), ('Consulting', 'Consulting'), ("Dean'S Approved Major", "Dean'S Approved Major"), ('Develop Genetics And Anatomy', 'Develop Genetics And Anatomy'), ('Contemporary Dance', 'Contemporary Dance'), ('Dentistry', 'Dentistry'), ('Dental Graduate', 'Dental Graduate'), ('Electrical Engineering', 'Electrical Engineering'), ('Aerospace Engineering', 'Aerospace Engineering'), ('Executive Mba', 'Executive Mba'), ('Biomedical Engineering', 'Biomedical Engineering'), ('E-Business', 'E-Business'), ('Chemical Engineering', 'Chemical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Clinical Engineering', 'Clinical Engineering'), ('Computer Engineering', 'Computer Engineering'), ('Economics', 'Economics'), ('Executive Doctorate In Mgmt', 'Executive Doctorate In Mgmt'), ('Teacher Education', 'Teacher Education'), ('Education', 'Education'), ('Electrical Engr & Appl Physics', 'Electrical Engr & Appl Physics'), ('Fluid & Thermal Science', 'Fluid & Thermal Science'), ('English', 'English'), ('Engineering Mechanics', 'Engineering Mechanics'), ('Engineering', 'Engineering'), ('Industrial Engineering', 'Industrial Engineering'), ('Economics Of Innovation & Tech', 'Economics Of Innovation & Tech'), ('Electronics', 'Electronics'), ('Macromolecular Science', 'Macromolecular Science'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Metallurgy & Materials Science', 'Metallurgy & Materials Science'), ('Materials Science & Engr', 'Materials Science & Engr'), ('Entrepreneurship', 'Entrepreneurship'), ('Environmental Engr (Adm Only)', 'Environmental Engr (Adm Only)'), ('Epidemiology & Biostatistics', 'Epidemiology & Biostatistics'), ('Engineering Physics', 'Engineering Physics'), ('Environmental Epidemiology', 'Environmental Epidemiology'), ('Engineering(Practice-Oriented)', 'Engineering(Practice-Oriented)'), ('Earth Sciences', 'Earth Sciences'), ('Systems Ctrl & Industrial Engr', 'Systems Ctrl & Industrial Engr'), ('Environmental Studies', 'Environmental Studies'), ('Systems & Control Engineering', 'Systems & Control Engineering'), ('Ethnic Studies', 'Ethnic Studies'), ('Evolutionary Biology', 'Evolutionary Biology'), ('Environmental Health Science', 'Environmental Health Science'), ('Exercise Physiology', 'Exercise Physiology'), ('Financial Analysis And Control', 'Financial Analysis And Control'), ('Family Medicine', 'Family Medicine'), ('French And Francophone Studies', 'French And Francophone Studies'), ('Financial Management', 'Financial Management'), ('Fin Reporting & Attestation', 'Fin Reporting & Attestation'), ('French', 'French'), ('French Studies', 'French Studies'), ('Financial Reporting', 'Financial Reporting'), ('German', 'German'), ('Genetics', 'Genetics'), ('Geological Sciences', 'Geological Sciences'), ('Gerontological Studies', 'Gerontological Studies'), ('German Studies', 'German Studies'), ('Geriatric Mental Health Nurs', 'Geriatric Mental Health Nurs'), ('General Medical Sciences', 'General Medical Sciences'), ('Genetics Counseling', 'Genetics Counseling'), ('Environmental Geology', 'Environmental Geology'), ('Ger Ment Hlth/Psyc Ment Hlth', 'Ger Ment Hlth/Psyc Ment Hlth'), ('Gerontological Nursing', 'Gerontological Nursing'), ('Modern Hebrew', 'Modern Hebrew'), ('Health Communication', 'Health Communication'), ('Human Development', 'Human Development'), ('Health Science', 'Health Science'), ('Health & Med Prof (Adm Only)', 'Health & Med Prof (Adm Only)'), ('History Of Policy Studies', 'History Of Policy Studies'), ('Health Systems Bioscience', 'Health Systems Bioscience'), ('Health Science Education', 'Health Science Education'), ('Health Systems Management', 'Health Systems Management'), ('History & Museum Studies', 'History & Museum Studies'), ('Hist & Phil Of Science/Tech', 'Hist & Phil Of Science/Tech'), ('Hist Of Science & Technology', 'Hist Of Science & Technology'), ('History', 'History'), ('Humanities', 'Humanities'), ('Integrated Biomedical Sciences', 'Integrated Biomedical Sciences'), ('Industrial Relations', 'Industrial Relations'), ('Integrated Graduate Studies', 'Integrated Graduate Studies'), ('International Management', 'International Management'), ('Information Systems', 'Information Systems'), ('International Management', 'International Management'), ('International Studies', 'International Studies'), ('Interior Design', 'Interior Design'), ('Italian', 'Italian'), ('Japanese', 'Japanese'), ('Judaic Studies', 'Judaic Studies'), ('Jd/Mba Joint Degree', 'Jd/Mba Joint Degree'), ('Japanese', 'Japanese'), ('Japanese Studies', 'Japanese Studies'), ('Jd/Mssa Joint Degree', 'Jd/Mssa Joint Degree'), ('Law & Public Policy', 'Law & Public Policy'), ('Law', 'Law'), ('Liberal Arts (Adm Only)', 'Liberal Arts (Adm Only)'), ('Labor & Human Resource Policy', 'Labor & Human Resource Policy'), ('Information & Library Science', 'Information & Library Science'), ('Library Science', 'Library Science'), ('Literature', 'Literature'), ('Llm - Us Legal Studies', 'Llm - Us Legal Studies'), ('Foreign Language (Adm Only)', 'Foreign Language (Adm Only)'), ('Llm - Tax', 'Llm - Tax'), ('Master Of Accountancy', 'Master Of Accountancy'), ('Mathematics And Physics', 'Mathematics And Physics'), ('Mgmt Advis Service', 'Mgmt Advis Service'), ('Mathematics', 'Mathematics'), ('Master In Business Admin', 'Master In Business Admin'), ('Molecular Biology & Microbiol', 'Molecular Biology & Microbiol'), ('Itn Mba Student', 'Itn Mba Student'), ('Roots Of Modern Consciousness', 'Roots Of Modern Consciousness'), ('Medical Technology', 'Medical Technology'), ('Medicine', 'Medicine'), ('Master Of Engineering & Mgmt', 'Master Of Engineering & Mgmt'), ('Metallurgy', 'Metallurgy'), ('Management', 'Management'), ('Management Info Systems', 'Management Info Systems'), ('Certificate In Mids', 'Certificate In Mids'), ('Marketing', 'Marketing'), ('Msms/Mba Joint Degree', 'Msms/Mba Joint Degree'), ('Molecular Medicine', 'Molecular Medicine'), ('Med Surg Nurs & Nurse Admin', 'Med Surg Nurs & Nurse Admin'), ('Master Of Nonprofit Org', 'Master Of Nonprofit Org'), ('Positive Organiz Devt & Chg', 'Positive Organiz Devt & Chg'), ('Public Health', 'Public Health'), ('Marketing And Policy Studies', 'Marketing And Policy Studies'), ('Management Science', 'Management Science'), ('Finance', 'Finance'), ('Information Systems', 'Information Systems'), ('Operations Research', 'Operations Research'), ('Medical-Surgical Nursing', 'Medical-Surgical Nursing'), ('Supply Chain Management', 'Supply Chain Management'), ('Medical Scientist Train Prog', 'Medical Scientist Train Prog'), ('Musicology', 'Musicology'), ('Doctor Musical Arts', 'Doctor Musical Arts'), ('Music Education', 'Music Education'), ('Music History', 'Music History'), ('Early Music Performance', 'Early Music Performance'), ('Music', 'Music'), ('Molecular Virology', 'Molecular Virology'), ('Acute Care Adult Nurs Pract', 'Acute Care Adult Nurs Pract'), ('Acute Care Nurse Practitioner', 'Acute Care Nurse Practitioner'), ('Nursing Administration', 'Nursing Administration'), ('Acute Care Nurpract/Flight Nur', 'Acute Care Nurpract/Flight Nur'), ('Acute Care Pediatric Nurs Prac', 'Acute Care Pediatric Nurs Prac'), ('Natural Sciences', 'Natural Sciences'), ('Nutritnl Biochem & Metabolism', 'Nutritnl Biochem & Metabolism'), ('Nursing Care Of Children', 'Nursing Care Of Children'), ('Nsg Care - Childbearing Family', 'Nsg Care - Childbearing Family'), ('Clinical Leadership, Nurs', 'Clinical Leadership, Nurs'), ('Cardiovascular Nursing', 'Cardiovascular Nursing'), ('Non Degree Itn Student', 'Non Degree Itn Student'), ('Neurosciences & Bioengineering', 'Neurosciences & Bioengineering'), ('Educational Leadership, Nurs', 'Educational Leadership, Nurs'), ('Neurosciences', 'Neurosciences'), ('Gerontological Cns', 'Gerontological Cns'), ('Infection Control', 'Infection Control'), ('Nursing Informatics', 'Nursing Informatics'), ('Nursing Management', 'Nursing Management'), ('Nurse Pract Prog - Adult', 'Nurse Pract Prog - Adult'), ('Family Nurse Practitioner', 'Family Nurse Practitioner'), ('Gerontological Nurse Pract', 'Gerontological Nurse Pract'), ('Nonprofit Management', 'Nonprofit Management'), ('Nurse Pract Prog - Neonatal', 'Nurse Pract Prog - Neonatal'), ('Nurse Pract Prog - Pediatric', 'Nurse Pract Prog - Pediatric'), ('Nutrition', 'Nutrition'), ('Nurse Anesthesia', 'Nurse Anesthesia'), ('Nurse-Midwifery', 'Nurse-Midwifery'), ('Nursing Doctor', 'Nursing Doctor'), ('Nursing', 'Nursing'), ('Organizational Administration', 'Organizational Administration'), ('Occupational Therapy', 'Occupational Therapy'), ("Organiz Dev'T & Leadership", "Organiz Dev'T & Leadership"), ('Organiz & Human Resource Devt', 'Organiz & Human Resource Devt'), ('Oncology', 'Oncology'), ('Operations Management', 'Operations Management'), ('Operations Research', 'Operations Research'), ('Optometry', 'Optometry'), ('Organizational Behavior', 'Organizational Behavior'), ('Organizational Dev & Analysis', 'Organizational Dev & Analysis'), ('Operations & Supply Chain Mgmt', 'Operations & Supply Chain Mgmt'), ('Psyc Ment Hlth/Nurs Admin', 'Psyc Ment Hlth/Nurs Admin'), ('Pre-Architecture', 'Pre-Architecture'), ('Pathology', 'Pathology'), ('Public Health Studies', 'Public Health Studies'), ('Predentistry (Adm Only)', 'Predentistry (Adm Only)'), ('Developmental Psychology', 'Developmental Psychology'), ('Perinatal Nursing', 'Perinatal Nursing'), ('Experimental Psychology', 'Experimental Psychology'), ('Professional Fellows Program', 'Professional Fellows Program'), ('Pharmacy', 'Pharmacy'), ('Biophysics And Bioengineering', 'Biophysics And Bioengineering'), ('Physical Education', 'Physical Education'), ('Philosophy', 'Philosophy'), ('Public Health Nutrition', 'Public Health Nutrition'), ('Physiology And Biophysics', 'Physiology And Biophysics'), ('Pharmacology', 'Pharmacology'), ('Physiology', 'Physiology'), ('Physical Therapy', 'Physical Therapy'), ('Prim Hlth Nurs Care Of Women', 'Prim Hlth Nurs Care Of Women'), ('Physics', 'Physics'), ('Prelaw (Adm Only)', 'Prelaw (Adm Only)'), ('Management Policy', 'Management Policy'), ('Post Masters Certification', 'Post Masters Certification'), ('Premedicine (Adm Only)', 'Premedicine (Adm Only)'), ('Physical Metallurgy', 'Physical Metallurgy'), ('Psychiatric-Mental Health Nurs', 'Psychiatric-Mental Health Nurs'), ('Psych-Mental Hlth Nurse Pract', 'Psych-Mental Hlth Nurse Pract'), ('Mental Retardation Rsrch Psyc', 'Mental Retardation Rsrch Psyc'), ('Prim Nurse Practitioner Prog', 'Prim Nurse Practitioner Prog'), ('Polymer Science & Engineering', 'Polymer Science & Engineering'), ('Political Science', 'Political Science'), ('Public Policy', 'Public Policy'), ('Psychology', 'Psychology'), ('Preveterinary (Adm Only)', 'Preveterinary (Adm Only)'), ('Reproductive Biology', 'Reproductive Biology'), ('Religion', 'Religion'), ('Religious Studies', 'Religious Studies'), ('Reg Nurs Baccalaureate', 'Reg Nurs Baccalaureate'), ('Reg Nurs Masters', 'Reg Nurs Masters'), ('Romance Languages', 'Romance Languages'), ('Russian', 'Russian'), ('Social Work - Bioethics', 'Social Work - Bioethics'), ('Social Work - 4Yr', 'Social Work - 4Yr'), ('Social Work - Is', 'Social Work - Is'), ('Social Work - Mssa/Jewish Comm', 'Social Work - Mssa/Jewish Comm'), ('Social Work/Law Joint Degree', 'Social Work/Law Joint Degree'), ('Social Work - Mssa/Phd', 'Social Work - Mssa/Phd'), ('Social Work - Is', 'Social Work - Is'), ('Social Work', 'Social Work'), ('Social Work - 3Yr', 'Social Work - 3Yr'), ('Social Work - Sr Yr Ab', 'Social Work - Sr Yr Ab'), ('Social Work - Mssa/Mba', 'Social Work - Mssa/Mba'), ('Social Wk/Mngt Non-Profit Orgn', 'Social Wk/Mngt Non-Profit Orgn'), ('Sociology', 'Sociology'), ('Spanish', 'Spanish'), ('Speech', 'Speech'), ('Social Policy History', 'Social Policy History'), ('Sports Medicine', 'Sports Medicine'), ('Social Sciences (Adm Only)', 'Social Sciences (Adm Only)'), ('Statistics', 'Statistics'), ('Strategic Management', 'Strategic Management'), ('Advanced Clinical Social Work', 'Advanced Clinical Social Work'), ('Social Welfare', 'Social Welfare'), ('Social Welfare Ph D  Program', 'Social Welfare Ph D  Program'), ('Systems Biology', 'Systems Biology'), ('Systems Physiology', 'Systems Physiology'), ('Tax', 'Tax'), ('Technology Management', 'Technology Management'), ('Technology(Medical,Lab,Dental)', 'Technology(Medical,Lab,Dental)'), ('Technology Entrepreneurship', 'Technology Entrepreneurship'), ('Theater Arts', 'Theater Arts'), ('Undergraduate Scholars Program', 'Undergraduate Scholars Program'), ('Non-Declared Major', 'Non-Declared Major'), ('Urban Studies', 'Urban Studies'), ('Womens Hlth Nurse Practitioner', 'Womens Hlth Nurse Practitioner'), ('World Literature', 'World Literature'), ("Women'S Studies", "Women'S Studies")], max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='resume',
            field=models.FileField(null=True, upload_to='resumes'),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Completed', 'Completed')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.AddField(
            model_name='room',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume_review.account'),
        ),
        migrations.AddField(
            model_name='room',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume_review.reviewer'),
        ),
        migrations.AddField(
            model_name='message',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume_review.account'),
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume_review.room'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_review.reviewer'),
        ),
    ]
