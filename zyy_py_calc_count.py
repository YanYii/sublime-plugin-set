# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
import json


class ZyyPyCalcCountCommand(sublime_plugin.TextCommand):
	''' 计算去重后的个数，以及去重前的总数 '''
	def run(self, edit):
		# 全选，分行
		# 记录总行数
		# 每一行 strip 后，记录
		# 计算出去重的后的个数
		# 输出结果
		region = sublime.Region(0, self.view.size())
		lines = self.view.lines(region)
		total_line = 'Total line: {:d}'.format(len(lines))
		print(total_line)
		d = {}
		for line in lines:
			content = self.view.substr(line).strip()
			if len(content) and content in d:
				d[content] += 1
			else:
				d[content] = 1
		
		# ensure_ascii 解决中文乱码
		json_str = json.dumps(d,sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
		result_panel = self.view.window().create_output_panel('result', False)
		characters = '\n统计结果：\n\n' + json_str + '\n'
		# 参数 force 为 True 才会显示文本
		result_panel.run_command('append',{'characters': characters, 'force': True, 'scroll_to_end': True})
		self.view.window().run_command('show_panel', {"panel": "output.result"})

