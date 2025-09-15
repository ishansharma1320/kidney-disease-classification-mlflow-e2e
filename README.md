# ML Project Template & MLOps

## File or Folder Structure
### ./
- `template.py` - Creates the template or folder structure and files inside it
- `requirements.txt` - Contains packages or dependencies for this project
- `setup.py` - Responsible for publishing this as a package on pypi, the SRC_REPO defined inside it is responsible for how importing would work and all

### ./src/cnnClassifier
- `__init__.py` - Here the things that should be common are defined like logging and all that
- `utils/common.py` - Here some utility functions are defined that could be accessed anywhere (@ensure_annotation on top of a function lets python know that parameters passed to it should be evaluated on a strict type basis)