import sublime
import sublime_plugin

last_command = None

class RepeatLastListener(sublime_plugin.EventListener):
  def on_window_command(self, window, command_name, args):
    global last_command

    if command_name == 'repeat_last':
      return

    last_command = [window, command_name, args]
    return

  def on_text_command(self, view, command_name, args):
    global last_command
    if command_name == 'repeat_last':
      return

    last_command = [view, command_name, args]
    return

class RepeatLast(sublime_plugin.WindowCommand):
  def run(self):
    global last_command
    if last_command == None:
      return

    last_command[0].run_command(last_command[1], last_command[2])