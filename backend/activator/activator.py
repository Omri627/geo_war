from activator.task import Task
import queue
import threading

class Activator:
    def __init__(self):
        # queue used to hold the tasks to activate.
        # the tasks filed in and the activator run them one after another
        self.tasks_queue = queue.Queue()

        # an event indicate that a new tasks filled the queue
        self.new_tasks_event = threading.Event()
        self.new_tasks_event.clear()

        # thread which checks if there is new tasks in the queue, get and activate them.
        # as long as the tasks queue is empty - the thread sleeps
        # whenever a new tasks comes along - the thread wakes up to execute the new tasks.
        self.thread_queue = threading.Thread(target=self.check_for_tasks)
        self.thread_queue.daemon = True
        self.thread_queue.start()


    def check_for_tasks(self):
        while True:
            # execute each task in the queue in FIFO order
            while not self.tasks_queue.empty():
                task = self.tasks_queue.get()
                task.activate()

            # wait for new tasks to arrive
            self.new_tasks_event.wait()

    # the method activate the new task by adding the task into activator queue
    def activate(self, method, arguments):
        # create task object
        task = Task(method=method, arguments=arguments)

        # add task into activator queue
        self.tasks_queue.put(task)
        if not self.new_tasks_event.is_set():
            self.new_tasks_event.set()

        # wait till the the task is completed
        return task.wait()
