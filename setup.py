from setuptools import setup, find_packages

setup(
    name="math_quiz",  # 你的包名
    version="0.1.0",   # 包的版本
    packages=find_packages(),  # 自动查找 math_quiz 目录下的所有包
    install_requires=[],  # 列出你的项目所依赖的外部库，如果没有则为空
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz',  # 运行命令 math_quiz 来启动游戏
        ],
    },
    description="A simple math quiz game",  # 项目的简短描述
    long_description=open('README.md').read(),  # 读取 README 文件的内容作为详细描述
    long_description_content_type='text/markdown',  # 设置 README 文件格式为 Markdown
    author="Yutong Liu",  # 你的名字
)