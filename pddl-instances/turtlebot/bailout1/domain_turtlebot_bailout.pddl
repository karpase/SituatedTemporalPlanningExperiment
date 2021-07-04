(define (domain turtlebot)

(:requirements :strips :typing :fluents :durative-actions :timed-initial-literals)

(:types
	waypoint robot - object
	printer - waypoint
)

(:functions 
	(bailout_distance)
	(distance ?a - waypoint ?b - waypoint)
)

(:predicates

	(bailout_available)
	(bailout_location ?to - waypoint)

	(robot_at ?v - robot ?wp - waypoint)
	(undocked ?v - robot)
	(docked ?v - robot)
	(localised ?v - robot)
	(dock_at ?wp - waypoint)

	;; Printing
	(carrying_papers ?r - robot)
	(nocarrying_papers ?r - robot)
	(asked_load ?r - robot)
	(asked_unload ?r - robot)
	(papers_delivered ?r - robot ?w - waypoint)
	(delivery_destination ?w - waypoint)
)

;; Bailout move
(:durative-action bailout
	:parameters (?v - robot ?to - waypoint)
	:duration ( = ?duration (+ 100 (* 5 (bailout_distance))))
	:condition (and
		(at start (bailout_location ?to))
		(at start (bailout_available))
		(at start (localised ?v))
		(over all (undocked ?v))
		)
	:effect (and
		(at start (not (bailout_available)))
		(at end (not (asked_load ?v)))
		(at end (not (asked_unload ?v)))
		(at end (robot_at ?v ?to))
		)
)

;; Move to any waypoint, avoiding terrain
(:durative-action goto_waypoint
	:parameters (?v - robot ?from ?to - waypoint)
	:duration ( = ?duration (* 5 (distance ?from ?to)))
	:condition (and
		(at start (robot_at ?v ?from))
		(at start (localised ?v))
		(over all (undocked ?v))
		)
	:effect (and
		(at start (not (robot_at ?v ?from)))
		(at end (not (asked_load ?v)))
		(at end (not (asked_unload ?v)))
		(at end (robot_at ?v ?to))
		)
)

;; Localise
(:durative-action localise
	:parameters (?v - robot)
	:duration ( = ?duration 60)
	:condition (over all (undocked ?v))
	:effect (at end (localised ?v))
)


;; Dock to charge
(:durative-action dock
	:parameters (?v - robot ?wp - waypoint)
	:duration ( = ?duration 30)
	:condition (and
		(over all (dock_at ?wp))
		(at start (robot_at ?v ?wp))
		(at start (undocked ?v)))
	:effect (and
		(at end (docked ?v))
		(at start (not (undocked ?v))))
)

(:durative-action undock
	:parameters (?v - robot ?wp - waypoint)
	:duration ( = ?duration 10)
	:condition (and
		(over all (dock_at ?wp))
		(at start (docked ?v)))
	:effect (and
		(at start (not (docked ?v)))
		(at end (undocked ?v)))
)

(:durative-action ask_load
	:parameters (?r - robot)
	:duration ( = ?duration 5)
	:condition (and
		(over all (nocarrying_papers ?r))
		(over all (exists (?p - printer) (robot_at ?r ?p)))
		)
	:effect (and
		(at end (asked_load ?r))
		)
)

(:durative-action ask_unload
	:parameters (?r - robot)
	:duration ( = ?duration 5)
	:condition (and
		(over all (carrying_papers ?r))
		(over all (exists (?w - waypoint) (and (delivery_destination ?w) (robot_at ?r ?w))))
		)
	:effect (and
		(at end (asked_unload ?r))
		)
)

(:durative-action wait_load
	:parameters (?r - robot)
	:duration ( = ?duration 15)
	:condition (and
		(at start (asked_load ?r))
		(at start (nocarrying_papers ?r))
		(over all (exists (?p - printer) (robot_at ?r ?p)))
		) 
	:effect (and
		(at end (carrying_papers ?r))
		(at end (not (nocarrying_papers ?r)))
		)
)

(:durative-action wait_unload
	:parameters (?r - robot ?w - waypoint)
	:duration ( = ?duration 15)
	:condition (and
		(at start (asked_unload ?r))
		(at start (carrying_papers ?r))
		(at start (delivery_destination ?w))
		(over all (robot_at ?r ?w))
		) 
	:effect (and
		(at end (not (carrying_papers ?r)))
		(at end (nocarrying_papers ?r))
		(at end (papers_delivered ?r ?w))
		)
)

)
