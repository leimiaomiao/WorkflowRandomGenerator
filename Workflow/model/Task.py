class Task(object):
    def __init__(self, task_id, pre_task_id_list, suc_task_id_list):
        self.task_id = task_id
        self.pre_task_id_list = pre_task_id_list
        self.suc_task_id_list = suc_task_id_list

        self.work_load = 0
        self.excu_time = None
        self.start_time = None
        self.end_time = None

    @property
    def workload(self):
        return self.work_load

    @workload.setter
    def workload(self, value):
        self.work_load = value

