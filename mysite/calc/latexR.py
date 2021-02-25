import jinja2
from jinja2 import Template

def render():
    print(os.path.abspath('.'))
    latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.')))
                                                            
    template = latex_jinja_env.get_template('test.tex')

    template_vars  = {}
    template_vars['section_1'] = 'The Section 1 Title'
    template_vars['section_2'] = 'The Section 2 Title'

# create a file and save the latex
    output_file = open('./generated_latex.tex', 'w')


render()    