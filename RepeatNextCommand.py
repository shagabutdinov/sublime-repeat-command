import sublime
import sublime_plugin

repeat_count = 0

class RepeatNextListener(sublime_plugin.EventListener):
  def __init__(self):
    self.repeating = False

  def on_modified_async(self, view):
    global repeat_count
    repeat_count = 0

  def on_text_command(self, view, command_name, args):
    global repeat_count

    if command_name == 'repeat_next' or self.repeating or repeat_count == 0:
      return

    self.repeating = True
    rng = repeat_count
    for _ in range(rng - 1):
      view.run_command(command_name, args)

    self.repeating = False
    repeat_count = 0

  def on_query_context(self, view, key, operator, operand, match_all):
    global repeat_count

    if key != 'will_repeat_next_command':
      return None

    will_repeat = repeat_count != 0
    if operator == sublime.OP_EQUAL:
      return operand == will_repeat

    if operator == sublime.OP_NOT_EQUAL:
      return operand != will_repeat

    raise Exception('Operator "' + operator + '" is not supported by ' +
      'context "' + will_repeat_next_command + '"')

class RepeatNext(sublime_plugin.WindowCommand):
  def run(self, count):
    global repeat_count
    if repeat_count == 0:
      repeat_count = ''

    repeat_count = int(str(repeat_count) + str(count))

class CancelRepeat(sublime_plugin.WindowCommand):
  def run(self):
    global repeat_count
    repeat_count = 0