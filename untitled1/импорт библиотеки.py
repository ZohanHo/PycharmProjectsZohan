# С шифтом правой в папке скачаной библиотеки, открыть в командной сторке py setup.py install




from gdsctools import anova, ic50_test
    an = anova(ic50_test, features_filename)  # second arg is optional
        an.anova_all()