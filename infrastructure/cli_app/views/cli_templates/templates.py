# I can use the same template and only one view, but
# this template then must use some template mechanism to be able to
# resolve a logic that I pass in it, like in Django. Idk if it is a
# good idea or not, because then this template will violate the
# open-closed principle.

calc_res_templ: str = 'The result is: %(output)d; date: %(date)s'
retr_saved_res_templ: str = 'Your saved results: %(output)s'
