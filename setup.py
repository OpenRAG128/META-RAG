from setuptools import setup, find_packages

setup(
    name='metarag',
    version='0.1.0',
    description='MetaRAG: A multi-LLM ensemble Retrieval-Augmented Generation framework with cosine similarity ranking.',
    author='Nisharg Nargund',
    author_email='nisharg@example.com',
    url='https://github.com/OpenRAG/metarag',
    packages=find_packages(),
    install_requires=[
        'langchain',
        'langchain_groq',
        'sentence-transformers',
        'faiss-cpu',
        'numpy',
        'PyPDF2',
        'scikit-learn'
    ],
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)