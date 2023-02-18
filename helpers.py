"""
    This module consist of helper functions 
"""
from collections import Counter
from models import State

def available_sessions(state: State, schedule: list ,already_assigned_educators: dict, \
                        already_assigned_sessions:dict, grade_index: int, period: int) -> list:
    """
        determines which sessions can be assigned to this particular slot without breaking the constraints

        steps:
        1. count the already assigned sessions
        2. get all the sessions for this grade
        3. remove sessions that have all their classes assigned
        4. remove sessions with teachers that have already been assigned in period
        5. remove sessions that have already been assigned in grade
    """

    assignments_count:Counter = Counter(schedule)

    result: dict = { key:value for (key, value) in state.sessions.items() \
                        if value.grade == state.grades[grade_index] }

    result = { key:value for (key, value) in result.items \
                        if assignments_count[key] < state.sessions[key].classes }

    result = { key:value for (key, value) in result.items() \
                        if key in already_assigned_sessions[grade_index] == False }

    result = { key:value for (key, value) in result.items() \
                        if value.educator in already_assigned_educators[period] == False }

    return list(result.keys())

def assign_session(state: State, schedule: list, session_id: int, already_assigned_educators: list, already_assigned_sessions: list, \
                            day_index: int, grade_index: int, period: int):
    """
        assigns a session to a single slot
    """

    index: int = state.schedule_index(day_index,grade_index,period)

    schedule[index] = session_id

    already_assigned_educators[period].add(state.sessions[session_id].educator)

    already_assigned_sessions[grade_index].add(session_id)

    pair_id: int = state.sessions[session_id].pair

    if pair_id != None:
        pair_grade_index: int = state.grades.index(state.sessions[pair_id].grade)
        
        pair_index: int = state.schedule_index(day_index,pair_grade_index,period)

        schedule[pair_index] = pair_id

        already_assigned_educators[period].add(state.sessions[pair_id].educator)

        already_assigned_sessions[pair_grade_index].add(pair_id)
