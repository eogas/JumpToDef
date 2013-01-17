import sublime_plugin
import re

reservedWords = ['instanceof', 'typeof', 'break', 'do', 'new', 'var', 'case', 'else', 'return', 'void', 'catch',
    'finally', 'continue', 'for', 'switch', 'while', 'this', 'with', 'debugger', 'function', 'throw', 'default', 'if',
    'try', 'delete', 'in']

namePattern = re.compile('^[_$\d\w][_$\d\w]*$')


class JumpToDefCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if (len(self.view.sel()) <= 0):
            return

        sel = self.view.sel()[0]
        if (sel.begin() == sel.end()):
            sel = self.view.word(self.view.sel()[0])
        else:
            sel = self.view.sel()[0]

        rawName = self.view.substr(sel)
        nameMatch = namePattern.match(rawName)

        if (nameMatch == None):
            return

        name = nameMatch.group(0)
        if (name in reservedWords):
            return

        funRegion = self.view.find('\s' + name + ':\sfunction\s?\(', 0)
        if (funRegion == None):
            return

        self.view.show_at_center(funRegion)
