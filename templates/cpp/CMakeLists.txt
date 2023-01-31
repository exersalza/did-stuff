cmake_minimum_required(VERSION 3.23)
project(%s VERSION 1.0 DESCRIPTION "Template created by exersalza" )

set(CMAKE_CXX_STANDARD 20)

aux_source_directory(src/ main)
aux_source_directory(src/source/* source)
aux_source_directory(src/include/* includes)

add_executable(${PROJECT_NAME} ${main} ${source} ${includes})