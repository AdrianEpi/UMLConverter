# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               main.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:25:53
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-01-16 12:41:19
#   @Description:        ...


from app.modules.uml_module.UMLConverter import UMLConverter

a = UMLConverter()
a.run()

# import esprima

# program = '''class Point {

#   /**
#    * @desc Creates a new point
#    * @param {int} coordinateX_ 
#    * @param {int} coordinateY_ 
#    */
#   constructor(coordinateX_, coordinateY_) {
#     this.coordinateX = coordinateX_;
#     this.coordinateY = coordinateY_;
#   }

#   /**
#    * @desc Returns the cordinateX
#    * @return The coordinateX
#    */
#   get_CoordinateX() {
#     return this.coordinateX;
#   }

#   /**
#    * @desc Returns the cordinateY
#    * @return The coordinateY
#    */
#   get_CoordinateY() {
#     return this.coordinateY;
#   }

#   /**
#    * @desc Sets the coordinateX
#    * @param {int} newCoord 
#    */
#   set_CoordinateX(newCoord) {
#     this.coordinateX = newCoord;
#   }

#   /**
#    * @desc Sets the coordinateY
#    * @param {int} newCoord 
#    */
#   set_CoordinateY(newCoord) {
#     this.coordinateY = newCoord;
#   }

#   /**
#    * @desc Draws a blue circle on canvas
#    * @param {element} ctx 
#    */
#   /* istanbul ignore next */
#   drawPoint(ctx, size, color) {
#     const RADIUS = size;
#     ctx.beginPath();
#     ctx.strokeStyle = color;
#     ctx.fillStyle = color;
#     ctx.arc(this.coordinateX, this.coordinateY, RADIUS, 0, 2 * Math.PI);
#     ctx.fill();
#     ctx.stroke();
#     ctx.closePath();
#   }

#   /**
#    * @desc Paints a white point to erase the old point of the canvas
#    * @param {element} ctx 
#    */
#   /* istanbul ignore next */
#   erasePoint(ctx, size) {
#     const RADIUS = size;
#     ctx.beginPath();
#     ctx.strokeStyle = 'WHITE';
#     ctx.fillStyle = 'WHITE';
#     ctx.arc(this.coordinateX, this.coordinateY, RADIUS, 0, 2 * Math.PI);
#     ctx.fill();
#     ctx.stroke();
#     ctx.closePath();
#   }
# }

# if (typeof require !== 'undefined') {
#   module.exports = { Point: Point };
# }
# '''

# print(esprima.parseScript(program))