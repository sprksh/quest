import os


"""
Cleartax lld test:
estimate lines of code
should return:
    empty lines
    code lines
    comment lines
    total lines

"""

""" Another test comment """
# Yet another

class CLOC:

    java_multiline_comment_start = '/*'
    java_multiline_comment_end = '*/'
    java_single_line_comment_start = '//'
    python_multiline_comment_start = ('"""', "'''")
    python_multiline_comment_end = ('"""', "'''")
    python_single_line_comment_start = '#'
    
    @staticmethod
    def cloc_simple(file, multiline_comment_start, multiline_comment_end, single_line_comment_start):
        """
        can be used with python and java
        """
        within_comment_block = False
        total = code = blank = comment = 0
        for i, line in enumerate(file):
            line = line.strip()
            total += 1
            if within_comment_block:
                comment += 1
                if line.endswith(multiline_comment_end):
                    within_comment_block = False
            elif line.startswith(multiline_comment_start):
                comment += 1
                if len(line) == 3 or not line.endswith(multiline_comment_end):
                    within_comment_block = True
            elif line.startswith(single_line_comment_start):
                comment += 1
            elif not line:
                blank += 1
        code = total - (comment + blank)
        return {
            "blank": blank, "comment": comment, "code": code, "total": total
            }

    @staticmethod
    def cloc_concrete_another():
        return {}

class LineCounter:
    def __init__(self):
        pass

    @staticmethod
    def get_language_from_file_name(file_path):
        extension = file_path.split('.')[-1]
        if extension == 'py':
            return 'python'
        if extension == 'java':
            return 'java'

    
    def count(self, file_path):
        language = self.get_language_from_file_name(file_path)
        file = open(file_path, 'r')
        # returns file_iterator
        count_dict = {}
        if language == 'python':
            count_dict = CLOC.cloc_simple(
                file, 
                CLOC.python_multiline_comment_start, 
                CLOC.python_multiline_comment_end,
                CLOC.python_single_line_comment_start
            )
        if language == 'java':
            count_dict = CLOC.cloc_simple(
                file, 
                CLOC.java_multiline_comment_start, 
                CLOC.java_multiline_comment_end,
                CLOC.java_single_line_comment_start
            )
        return language, count_dict


class LinesOfCodeEstimator:
    def __init__(self):
        self.estimate = {}
    
    def update_estimate(self, language, count_dict):
        if language and language not in self.estimate:
            self.estimate[language] = count_dict
        else:
            for k, v in count_dict.items():
                self.estimate[language][k] += v
    
    def estimate_lines_of_code_in_path(self, path):
        # print(path)
        if os.path.isfile(path):
            language, count_dict = LineCounter().count(path)
            self.update_estimate(language, count_dict)
            return
        
        for entry in os.listdir(path):
            if entry.startswith('.'):
                continue
            entry = os.path.join(path, entry)
            self.estimate_lines_of_code_in_path(entry)
        return self.estimate
