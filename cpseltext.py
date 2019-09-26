import sublime
import sublime_plugin


class Cpseltext(sublime_plugin.TextCommand):
	def run(self, edit):
		print("cpseltext loaded")
		selection = self.view.sel()
		begin = selection[0].begin()
		end = selection[0].end()
		character_num = end - begin
		text = self.view.substr(sublime.Region(begin, end))
		if int(character_num) >= 2:
			sublime.set_clipboard(text)

