import copy


def lab_1():
    class LearningBasicClasses:
        @staticmethod
        def first_method():
            print("The first method is working")

        @staticmethod
        def second_method():
            print("The second method is working too")

    LearningBasicClasses.first_method()
    LearningBasicClasses.second_method()

    class Employee:
        employee_count = 0

        def __init__(self, name, salary):
            self.name = name
            self.salary = salary
            Employee.employee_count += 1

        def print_name(self):
            print(self.name)

        def print_salary(self):
            print(self.salary)

        @staticmethod
        def print_employee_count():
            print(Employee.employee_count)

    luke = Employee("Luke", 2000)
    han = Employee("Han", 5000)

    luke.print_name()
    luke.print_salary()

    han.print_name()
    han.print_salary()

    Employee.print_employee_count()

    class Point:

        def __init__(self):
            self.x = 0
            self.y = 0

        def __str__(self):
            return "Point x: " + str(self.x) + "\n Point y: " + str(self.y)

        def get_sum(self):
            return self.x + self.y

        def add_point(self, to_add):
            self.x, self.y = to_add

        def __add__(self, new_point):
            to_add = self.x, self.y
            return to_add + new_point

    coords = 10, 20

    p1 = Point()
    p1.add_point(coords)
    print(p1.get_sum())

    coords2 = 2, 4
    p2 = Point()
    p2.add_point(coords2)

    # p3 = p1+p2
    # print(p3)

    def square(i):
        return i*i

    print(square(3))

    def next_square():
        i = 1
        while True:
            yield i*i
            i += 1

    sq = next_square()
    for i in range(100):
        print(next(sq))

    graph = {'A': {'B', 'C'},
             'B': {'A', 'D', 'E'},
             'C': {'A', 'F'},
             'D': {'B'},
             'E': {'B', 'F'},
             'F': {'C', 'E'}}

    def dfs(new_graph, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(new_graph[vertex] - visited)
        return visited
    print(dfs(graph, "B"))

    def dfs_paths(new_graph, start, goal):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in new_graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))

    print(list(dfs_paths(graph, 'F', 'D')))

if __name__ == '__main__':
    lab_1()
