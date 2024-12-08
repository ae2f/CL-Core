import mod.ae2fPy.PreP.PreP as PreP
import os
import sys
import pathlib
import subprocess


HERE = os.path.dirname(os.path.abspath(__file__))
GIVEN_PATH = HERE if len(sys.argv) != 3 else sys.argv[1]
GIVEN_CL_PATH = HERE if len(sys.argv) != 3 else sys.argv[2]

PRM_INCLUDE = f"{HERE}/pyinclude/"

print("Hello World! BmpCLConfig is running...")
print(f"Current Position: {HERE}")
print(f"Given Path: {GIVEN_PATH}")


# Preprocess 0: Get all source and throw it to ...cl
for file in (f for f in pathlib.Path(f'{GIVEN_PATH}/').rglob('*.cl.c') if f.is_file()):
    OUT_NAME = str(file.absolute())[:-2:]
    OUT_NAME_TMP = OUT_NAME + '.tmp.c'

    IN_CTN : list[str]
    with open(file, 'r') as F:
        IN_CTN = F.readlines()
        F.close()

    with open(OUT_NAME_TMP, 'w') as F:
        F.writelines([
            "#define ae2fCL_LocAsCL\n",
            "#define _GCC_WRAP_STDINT_H\n",
            "#define _MATH_H\n",
            "#define ae2f_Cmp_Fun_h\n",
            "#define __STDC_HOSTED__ 0\n"
        ])
        F.writelines(IN_CTN)
        F.close()

    result = subprocess.run(['gcc', '-Wno-error', '-E', '-P', '-I' + PRM_INCLUDE, '-I' + GIVEN_CL_PATH, OUT_NAME_TMP, '-o', OUT_NAME])
    print(result.stdout)
