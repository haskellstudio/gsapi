/*
  ==============================================================================

    GSPatternEventPyWrap.h
    Created: 19 Jun 2016 6:52:46pm
    Author:  Martin Hermant

  ==============================================================================
*/

#ifndef GSPATTERNEVENTPYWRAP_H_INCLUDED
#define GSPATTERNEVENTPYWRAP_H_INCLUDED

#include "PythonUtils.h"
#include "GSPatternEvent.h"


class GSPatternEventPyWrap{
public:

  GSPatternEventPyWrap(){
    init();
  }
  ~GSPatternEventPyWrap(){
    Py_DECREF(TagsObjName);
    Py_DECREF(DurationObjName);
    Py_DECREF(StartObjName);
    Py_DECREF(PitchObjName);
    Py_DECREF(VelocityObjName);
  }

  void init(){


    StartObjName = PyString_FromString("startTime");
    DurationObjName = PyString_FromString("duration");
    PitchObjName = PyString_FromString("pitch");
    VelocityObjName = PyString_FromString("velocity");
    TagsObjName = PyString_FromString("tags");

  }

  GSPatternEvent* GenerateFromObj(PyObject* o){
    GSPatternEvent * e = nullptr;
    PyObject ** obj = _PyObject_GetDictPtr(o);
    if(!obj){DBG("weird class passed back"); return nullptr;}
    PyObject * dict = *obj;
    if(!PyDict_Check(dict)){DBG("no dict passed back");}
    else{
      e = new GSPatternEvent();
      {
        PyObject * n = PyDict_GetItem(dict, StartObjName);
        if(n){e->start = PyFloat_AsDouble(n);}
      }
      {
        PyObject * n = PyDict_GetItem(dict, DurationObjName);
        if(n){e->duration = PyFloat_AsDouble(n);}
      }

      {
        PyObject * n = PyDict_GetItem(dict, PitchObjName);
        if(n){e->pitch = PyInt_AsLong(n);}
      }

      {
        PyObject * n = PyDict_GetItem(dict, VelocityObjName);
        if(n){e->velocity = PyInt_AsLong(n);}
      }

    }



    return e;
  }

  PyObject*  TagsObjName ;
  PyObject*  DurationObjName ;
  PyObject*  StartObjName ;
  PyObject*  PitchObjName ;
  PyObject*  VelocityObjName ;
  
  
};



#endif  // GSPATTERNEVENTPYWRAP_H_INCLUDED