# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               main.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:25:53
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-01-16 21:14:49
#   @Description:        ...


# from app.modules.uml_module.UMLConverter import UMLConverter

# a = UMLConverter()
# a.run()

import esprima

aaa = '''
class Point {

  constructor(coordinateX_, coordinateY_) {
    this.coordinateX = coordinateX_;
    this.coordinateY = coordinateY_;
  }


  get_CoordinateX() {
    return this.coordinateX;
  }

  /**
  get_CoordinateY() {
    return this.coordinateY;
  }

  set_CoordinateX(newCoord) {
    this.coordinateX = newCoord;
  }


  set_CoordinateY(newCoord) {
    this.coordinateY = newCoord;
  }


  drawPoint(ctx, size, color) {
    const RADIUS = size;
    ctx.beginPath();
    ctx.strokeStyle = color;
    ctx.fillStyle = color;
    ctx.arc(this.coordinateX, this.coordinateY, RADIUS, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();
    ctx.closePath();
  }


  erasePoint(ctx, size) {
    const RADIUS = size;
    ctx.beginPath();
    ctx.strokeStyle = 'WHITE';
    ctx.fillStyle = 'WHITE';
    ctx.arc(this.coordinateX, this.coordinateY, RADIUS, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();
    ctx.closePath();
  }**/
}

class Point2 {

  constructor(coordinateX_, coordinateY_) {
    this.coordinateX = coordinateX_;
    this.coordinateY = coordinateY_;
  }


  get_CoordinateX() {
    return this.coordinateX;
  }

  /**
  get_CoordinateY() {
    return this.coordinateY;
  }

  set_CoordinateX(newCoord) {
    this.coordinateX = newCoord;
  }


  set_CoordinateY(newCoord) {
    this.coordinateY = newCoord;
  }


  drawPoint(ctx, size, color) {
    const RADIUS = size;
    ctx.beginPath();
    ctx.strokeStyle = color;
    ctx.fillStyle = color;
    ctx.arc(this.coordinateX, this.coordinateY, RADIUS, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();
    ctx.closePath();
  }


  erasePoint(ctx, size) {
    const RADIUS = size;
    ctx.beginPath();
    ctx.strokeStyle = 'WHITE';
    ctx.fillStyle = 'WHITE';
    ctx.arc(this.coordinateX, this.coordinateY, RADIUS, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();
    ctx.closePath();
  }**/
}
'''

#print(esprima.parseScript(aaa))
l = esprima.parseScript(aaa)
print(l)
# for i in l.body:
# 	print(i)