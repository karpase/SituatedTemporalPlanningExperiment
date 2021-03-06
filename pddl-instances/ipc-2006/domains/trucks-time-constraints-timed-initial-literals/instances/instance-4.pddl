(define (problem truck-4)
(:domain Trucks-TimeTIL)
(:objects
	truck1 - truck
	package1 - package
	package2 - package
	package3 - package
	package4 - package
	package5 - package
	package6 - package
	l1 - location
	l2 - location
	l3 - location
	a1 - truckarea
	a2 - truckarea)

(:init
	(at truck1 l2)
	(free a1 truck1)
	(free a2 truck1)
	(closer a1 a2)
	(at package1 l2)
	(at package2 l2)
	(at package3 l3)
	(at package4 l3)
	(at package5 l3)
	(at package6 l3)
	(connected l1 l2)
	(connected l1 l3)
	(connected l2 l1)
	(connected l2 l3)
	(connected l3 l1)
	(connected l3 l2)
	(deliverable package1 l3)
	(deliverable package4 l1)
	(deliverable package6 l2)
	(at 537.3 (not (deliverable package1 l3)))
	(at 1026.9 (not (deliverable package4 l1)))
	(at 2878.2 (not (deliverable package6 l2)))
	(= (drive-time l1 l2) 792.7)
	(= (drive-time l1 l3) 445.1)
	(= (drive-time l2 l1) 792.7)
	(= (drive-time l2 l3) 488.4)
	(= (drive-time l3 l1) 445.1)
	(= (drive-time l3 l2) 488.4))

(:goal (and 
	(delivered package1 l3)
	(at-destination package2 l3)
	(at-destination package3 l1)
	(delivered package4 l1)
	(at-destination package5 l1)
	(delivered package6 l2)))

(:metric minimize (total-time))

)
