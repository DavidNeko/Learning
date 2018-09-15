# encoding = utf-8

def make_menu(menu_list):
    menu = []
    selections = {}
    for index, item, callback in menu_list:
        menu.append('{}. {}'.format(index, item.title()))
        selections[str(index)] = callback
    menu.append('>> ')
    return '\n'.join(menu), selections

class Task_Runner(object):
    """
    运行测试用的任务进程
    """

    def __init__(self):
        self.pid_list = []

    def _run_process(self, cmds):
        process = Popen(cmds)
        self.pid_list.append(process.pid)

    def run_test_problem_001(self):
        cmd = os.path.sep.join([
            'test_problem_001.py'
        ])
        self._run_process([sys.executable, cmd])
