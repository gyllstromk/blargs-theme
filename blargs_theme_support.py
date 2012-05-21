from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


class BlargsStyle(Style):
    background_color = "red"
    default_style = ""

    styles = {
        # No corresponding class for the following:
        #Text:                     "", # class:  ''
        Whitespace:                "underline #f8f8f8",      # class: 'w'
        Error:                     "#a40000 border:#ef2929", # class: 'err'
        Other:                     "#000000",                # class 'x'

        Comment:                   "italic #73C6EF", # class: 'c'
        Comment.Preproc:           "noitalic",       # class: 'cp'

        Keyword:                   "bold #FF0000",   # class: 'k'
        Keyword.Constant:          "bold #FF0000",   # class: 'kc'
        Keyword.Declaration:       "bold #FF0000",   # class: 'kd'
        Keyword.Namespace:         "bold #FF0000",   # class: 'kn'
        Keyword.Pseudo:            "bold #FF0000",   # class: 'kp'
        Keyword.Reserved:          "bold #FF0000",   # class: 'kr'
        Keyword.Type:              "bold #FF0000",   # class: 'kt'

        Operator:                  "#582800",   # class: 'o'
        Operator.Word:             "bold #004461",   # class: 'ow' - like keywords

        Punctuation:               "bold #000000",   # class: 'p'

        # because special names such as Name.Class, Name.Function, etc.
        # are not recognized as such later in the parsing, we choose them
        # to look the same as ordinary variables.
        Name:                      "#FFFF8e",        # class: 'n'
        Name.Attribute:            "#c4a000",        # class: 'na' - to be revised
        Name.Builtin:              "#004461",        # class: 'nb'
        Name.Builtin.Pseudo:       "#3465a4",        # class: 'bp'
        Name.Class:                "#000000",        # class: 'nc' - to be revised
        Name.Constant:             "#000000",        # class: 'no' - to be revised
        Name.Decorator:            "#888",           # class: 'nd' - to be revised
        Name.Entity:               "#ce5c00",        # class: 'ni'
        Name.Exception:            "bold #cc0000",   # class: 'ne'
        Name.Function:             "#000000",        # class: 'nf'
        Name.Property:             "#000000",        # class: 'py'
        Name.Label:                "#f57900",        # class: 'nl'
        Name.Namespace:            "#000000",        # class: 'nn' - to be revised
        Name.Other:                "#000000",        # class: 'nx'
        Name.Tag:                  "bold #004461",   # class: 'nt' - like a keyword
        Name.Variable:             "#000000",        # class: 'nv' - to be revised
        Name.Variable.Class:       "#000000",        # class: 'vc' - to be revised
        Name.Variable.Global:      "#000000",        # class: 'vg' - to be revised
        Name.Variable.Instance:    "#000000",        # class: 'vi' - to be revised

        Number:                    "#990000",        # class: 'm'

        Literal:                   "#73C6EF",        # class: 'l'
        Literal.Date:              "#73C6EF",        # class: 'ld'

        String:                    "#73C6EF",        # class: 's'
        String.Backtick:           "#73C6EF",        # class: 'sb'
        String.Char:               "#73C6EF",        # class: 'sc'
        String.Doc:                "italic #8f5902", # class: 'sd' - like a comment
        String.Double:             "#73C6EF",        # class: 's2'
        String.Escape:             "#73C6EF",        # class: 'se'
        String.Heredoc:            "#73C6EF",        # class: 'sh'
        String.Interpol:           "#73C6EF",        # class: 'si'
        String.Other:              "#73C6EF",        # class: 'sx'
        String.Regex:              "#73C6EF",        # class: 'sr'
        String.Single:             "#73C6EF",        # class: 's1'
        String.Symbol:             "#73C6EF",        # class: 'ss'

        Generic:                   "#FFFF8e",        # class: 'g'
        Generic.Deleted:           "#a40000",        # class: 'gd'
        Generic.Emph:              "italic #000000", # class: 'ge'
        Generic.Error:             "#ef2929",        # class: 'gr'
        Generic.Heading:           "bold #000080",   # class: 'gh'
        Generic.Inserted:          "#00A000",        # class: 'gi'
        Generic.Output:            "#888",           # class: 'go'
        Generic.Prompt:            "#745334",        # class: 'gp'
        Generic.Strong:            "bold #000000",   # class: 'gs'
        Generic.Subheading:        "bold #800080",   # class: 'gu'
        Generic.Traceback:         "bold #a40000",   # class: 'gt'
    }
