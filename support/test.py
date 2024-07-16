import os


def make_directory(name: int, site: str)-> None :
    """./site/name/ 파일 구조를 생성한다.

    Args:
        name (int): 문제 번호
        site (str): 풀 문제의 사이트
    """
    if site not in ["baekjoon", "programmers"] :
        raise NameError("site이름 재확인")
    path = f"C:/workspace/coding_test/{site}/{name}"
    os.mkdir(path)
    