#define ae2fCL_Scenario
#ifndef ae2fCL_Loc_h
#define ae2fCL_Loc_h


#ifndef ae2fCL_LocAsCL

/// @brief opencl keyword
#define __kernel

/// @brief opencl keyword
#define __global


#ifndef ae2fCL_Scenario
#pragma message ("You did not choose the scenario. Fetching the interface...")
#if !(defined(ae2fCL_Scenario_h) || defined(ae2fCL_Scenario))
#define ae2fCL_Scenario_h

#define get_global_id(i) 0
#define get_global_size(i) 0

#endif
#endif

/// @brief
/// Shows when the code is running on CL code, not C.
#define ae2fCL_whenCL(...)

/// @brief
/// Shows when the code is running on C, not CL.
#define ae2fCL_whenC(...) __VA_ARGS__

#else
typedef int int32_t;
typedef uint uint32_t;

typedef short int16_t;
typedef ushort uint16_t;

typedef char int8_t;
typedef uchar uint8_t;

/// @brief
/// Shows when the code is running on CL code, not C.
#define ae2fCL_whenCL(...) __VA_ARGS__

/// @brief
/// Shows when the code is running on C, not CL.
#define ae2fCL_whenC(...)

#endif

/// @brief pointer type for host code
#define ae2fCL_HostPtr(__flag, __type) ae2fCL_whenC(cl_mem) ae2fCL_whenCL(__flag __type*)

#endif
