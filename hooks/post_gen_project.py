#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('post_gen_project')

import shutil
import os

ROOT = os.getcwd()
DOC_SOURCES = 'doc_sources'
DOCS = 'docs'
DOC_TYPE_FILES_MAP = {
    'mkdocs': ['index.md', '/mkdocs.yml'],
    'sphinx': ['conf.py', 'index.rst', 'make.bat', 'Makefile']
}

def move_doc_files(which):
    logger.info('Initializing docs for %s' % which)
    if not os.path.exists(DOCS):
        os.mkdir(DOCS)
    for item in DOC_TYPE_FILES_MAP[which]:
        dst, name = (ROOT, item[1:]) if item.startswith('/') else (DOCS, item)
        src_path = os.path.join(DOC_SOURCES, which, name)
        dst_path = os.path.join(dst, name)
        logger.info('Moving %s to %s.' % (src_path, dst_path))
        if os.path.exists(dst_path):
            os.unlink(dst_path)
        os.rename(src_path, dst_path)

{% if cookiecutter.docs_tool == "mkdocs" %}

move_doc_files("mkdocs")

{% elif cookiecutter.docs_tool == "sphinx" %}

move_doc_files("sphinx")

{% endif %}

logger.info("Removing all temporary documentation sources")
shutil.rmtree(DOC_SOURCES)

logger.info('Removing all temporary license files')
shutil.rmtree('licenses')

logger.info('Removing jinja2 macros')
shutil.rmtree('macros')
