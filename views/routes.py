from views.Router import Router, DataStrategyEnum
from views.main_menu_view import MainMenuView
from views.register_student_view import RegisterStudentView

router = Router(DataStrategyEnum.QUERY)

router.routes = {
  "/": MainMenuView,
  "/register": RegisterStudentView
}