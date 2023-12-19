import SimpleITK as sitk


def BSplineFun(fixed_image,moving_image):
    control_point = 3
    order = 1

    registration_method = sitk.ImageRegistrationMethod()
    #Metrics
    registration_method.SetMetricAsCorrelation()
    #registration_method.SetMetricSamplingStrategy(registration_method.RANDOM)
    registration_method.SetMetricSamplingPercentage(0.3)
    #Optimizer
    registration_method.SetOptimizerAsRegularStepGradientDescent(learningRate=0.1, minStep=1e-4, numberOfIterations=200)
    bspline_transform = sitk.BSplineTransformInitializer(fixed_image, transformDomainMeshSize=[control_point]*fixed_image.GetDimension(), order=order)
    registration_method.SetInitialTransform(bspline_transform, inPlace=False)
    registration_method.SetShrinkFactorsPerLevel([4, 2, 1])
    registration_method.SetSmoothingSigmasPerLevel([2, 1, 0])

    # Perform the registration
    final_transform = registration_method.Execute(fixed_image, moving_image)
    evaluation_metric = registration_method.GetMetricValue()
    initial_metric_value = registration_method.MetricEvaluate(fixed_image, moving_image)
    print(f"Initial metric value: {initial_metric_value}")
    print(f"Final metric value: {evaluation_metric}")

    return final_transform